import os
import sys
import traceback
from datetime import datetime

import bson
import pymongo
import re
from pymongo import MongoClient
from multiprocessing import Process


def logger(col_name, fl_name, msg):
    logger_file_name = os.path.basename(
        sys.argv[0])[:-3] + "_" + col_name + fl_name + ".txt"
    with open(logger_file_name, "a") as f:
        f.write(msg)
        f.write("\n")


def get_last_id(col_name, file_name):
    with open(file_name, 'r') as f:

        index = -1
        while True:
            _id = f.readlines()[index].strip()
            if len(_id) == 24:
                return _id

            logger(col_name, "_LoggerMsg",
                   f"Get the {-index} th _id error; Current _id: {_id}")
            index -= 1


def find_documents(write_conn, data_base, collection, query, projection, sort_key="_id", sort_value=pymongo.ASCENDING,
                   limits=0):
    _docs = write_conn[data_base][collection].find(
        query, projection).sort(sort_key, sort_value).limit(limits)
    docs = [item for item in _docs]
    return docs


def main(read_uri, write_uri, more_filter, col_name, db_name, starts='', ends='', limits=10000):
    start_id = ''
    current_id = ''
    exception_count = 0
    has_query_count = 0
    has_read_id_count = 0
    read_conn = MongoClient(host=read_uri)
    write_conn = MongoClient(host=write_uri)
    current_file_name = os.path.basename(sys.argv[0])[:-3] + "_" + col_name

    if os.path.exists(f"{current_file_name}_HasReadIds.txt"):
        try:
            start_id = get_last_id(
                col_name, f"{current_file_name}_HasReadIds.txt")
        except Exception as e:
            msg = str(e) + ",trace:" + traceback.format_exc()
            logger(col_name, "_LoggerMsg",
                   f"Failed to get last id, exit! Error Msg {msg}.")
            sys.exit()

    if not start_id:
        one_doc = write_conn[db_name][col_name].find(
            {}, projection={"_id": 1}).sort("_id", pymongo.ASCENDING)
        start_id = one_doc[0]["_id"]
        logger(col_name, '_HasReadIds', str(start_id))

    if not ends:
        ends = write_conn[db_name][col_name].find({}, projection={"_id": 1}).sort(
            "_id", pymongo.DESCENDING).limit(1)[0]["_id"]

    end_id = bson.ObjectId(ends)
    query = {"_id": {"$gte": bson.ObjectId(start_id)}}

    if starts:
        query = {"_id": {"$gte": bson.ObjectId(starts)}}

    if more_filter:
        query.update(more_filter)

    while exception_count < 20:

        has_query_count += 1
        docs = find_documents(write_conn, db_name, col_name,
                              query, None, "_id", pymongo.ASCENDING, limits)
        logger(col_name,
               "_LoggerMsg",
               f"******************** Has queried {has_query_count}*{limits}={has_query_count * limits}  documents. Time: {datetime.today()}. ********************")

        try:
            if not docs:
                logger(col_name,
                       "_LoggerMsg", f"Empty docs, exits! Time:{datetime.today()}, last _id is: {current_id}.")
                return

            for doc in docs:

                _id = doc.get("_id")
                current_id = _id

                if current_id > end_id:
                    logger(col_name,
                           "_LoggerMsg",
                           f"Get end point, and mission is over! Time:{datetime.today()}, last _id is: {current_id}.")
                    return

                has_read_id_count += 1
                if not has_read_id_count % 1000:
                    logger(col_name, "_HasReadIds", str(current_id))

                fix_data(doc, col_name, write_conn, read_conn, db_name)

                query["_id"] = {"$gt": current_id}

        except Exception as e:
            query["_id"] = {"$gt": current_id}
            logger(col_name,
                   "_LoggerMsg", f'Get error, exception msg is {str(e) + ",trace:" + traceback.format_exc()}, Time: {datetime.today()}, current _id is: {current_id}.')
            exception_count += 1

    logger(col_name, "_LoggerMsg",f"Catch exception 20 times, mission is over. Ending time:{datetime.today()}, Last _id is: {current_id}.")


def fix_data(doc, col_name, write_conn, read_conn, db_name):
    if (col_name == "collection1") and (doc.get("col1")):
        write_conn[db_name][col_name].update({"_id": doc.get("_id")}, {
            "$set": {"col2": 5}})
        return
    if not doc.get("col3"):
        return
    col3 = doc.get("col3")
    uid = doc.get("UID")
    cc_doc = read_conn.database.collection.find(
        {"col4": col3, "UID": uid}, projection={"type": 1}).sort("type", 1).limit(1)
    cc_type = 0
    for cc_per in cc_doc:
        cc_type = cc_per["type"]
    if not cc_type:
        cc_type = find_type_by_regex(cc_type, col3)
    write_conn[db_name][col_name].update({"_id": doc.get("_id")}, {
        "$set": {"col5": cc_type}})


def find_type_by_regex(cc_type, col3):
    phone_regex = "^1(3|4|5|7|8)\d{9}$"
    fixed_regex = "[0-9]{4,11}"
    if re.match(phone_regex, col3):
        cc_type = 5
        return cc_type
    if "@" in col3:
        cc_type = 6
        return cc_type
    if re.match(fixed_regex, col3):
        cc_type = 7
    if not cc_type:
        cc_type = 8
    return cc_type

def sandbox(collection_name):  #测试环境是一个数据源
    uri = "mongodb://***********"
    start = ""
    end = ""
    more_filter = {}
    limit = 500
    # 4个集合同时清洗时，开启多进程处理
    process_list = []
    if not collection_name:
        for col in collection_list:
            p = Process(target=main, args=(uri, more_filter, col, "database_name",
                                           start, end, limit))
            p.start()
            process_list.append(p)
        for process in process_list:
            process.join()

    else:
        main(uri, more_filter, collection_name, "database_name", start, end, limit)


def online(collection_name, limit=1000):  #正式环境是多数据源
    write_uri = "mongodb://************"  #需修改为线上配置
    read_uri = "mongodb://*************"   #需修改为线上配置
    more_filter = {}
    # 4个集合同时清洗开启多进程处理
    process_list = []
    if not collection_name:
        for col in collection_list:
            p = Process(target=main, args=(read_uri, write_uri, more_filter, col, "database", "", "", limit))
            p.start()
            process_list.append(p)
        for process in process_list:
            process.join()

    else:
        main(read_uri, write_uri, more_filter, collection_name, "database", "", "", limit)


def func(environment, collection_name):
    env = ["sandbox", "online"]
    if not environment:
        print("environment is null , please check !")
        return
    if not collection_name:
        if (environment == "sandbox"):
            sandbox("")
        else:
            if environment == "online":
                online("")
        return
    if (environment not in env) or (collection_name not in collection_list):
        print("Param is wrong , please check !")
        return
    if (environment == "sandbox"):
        sandbox(collection_name)
    else:
        if environment == "online":
            online(collection_name)


if __name__ == '__main__':
    collection_list = ["collection1", "collection2", "collection3", "collection4","collection5"]
    # {sandbox,online},{"collection1", "collection2", "collection3", "collection4","collection5"}
    func("sandbox", "")
    pass
