
$push(数组更新操作符)

一、定义
$push操作符作用是在数组后面拼接特定值。
$push操作形式：
```
{ $push: { <field1>: <value1>, ... } }
```

用点表示法区分<field>是嵌入式文档还是数组。

二、行为

如果field不在文档的更新字段中，$push直接将field以元素的形式新增进文档中。

如果field不是数组，操作失败。

如果value是一个数组，$push将整个数组以单元素拼接到文档。用$each操作符配合$push实现单独新增value里的每个元素。



场景：
collection：ThirdManufacturers
data-form：
```
{ 
    "_id" : ObjectId("5ce7b93028b5b44f33c18993"), 
    "logo" : "93ea1f8d0056ca4d1024746f6087cae5.png", 
    "accessibleMenu" : [
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "userManagement"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5ce7b93028b5b44f33c18994"), 
    "logo" : "9ac127a744b79d8857ef403515508eac.png", 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d312a88b6eca17a97c1b24a"), 
    "logo" : "0fd96b4ed0caeb4c310f9ce716080d43.png", 
    "accessibleMenu" : [
        "userManagement", 
        "userCenter", 
        "mapSearch" 
    ]
}
```

1、在accessibleMenu数组增加元素【retreatSafely】：
```
db.getCollection("ThirdManufacturers").update(
   { _id : ObjectId("5d312a88b6eca17a97c1b24a") },
   { $push: { accessibleMenu: "retreatSafely" } }
)
```
结果：
```
{ 
    "_id" : ObjectId("5d312a88b6eca17a97c1b24a"), 
    "logo" : "0fd96b4ed0caeb4c310f9ce716080d43.png", 
    "accessibleMenu" : [
        "userManagement", 
        "userCenter", 
        "mapSearch", 
        "retreatSafely"
    ]
}
```

2、删除accessibleMenu数组中元素【retreatSafely】：
```
db.getCollection("ThirdManufacturers").update({"_id":ObjectId("5d312a88b6eca17a97c1b24a")},{$pull:{accessibleMenu:{$in:["retreatSafely"]}}})
```




