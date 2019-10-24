

```
db.getCollection("ThirdManufacturers").find(, {_id:1,accessibleMenu:1}).limit(3)


{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba73e"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba73f"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba740"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement"
    ]
}

```

```
增加accessibleMenu数组元素：
全部：
db.getCollection("ThirdManufacturers").updateMany(
   {},
   { $push: { accessibleMenu: "retreatSafely" } }
)
单个：
db.getCollection("ThirdManufacturers").update(
   { _id : ObjectId("5ce7b93028b5b44f33c18993") },
   { $push: { accessibleMenu: "retreatSafely" } }
)




db.getCollection("ThirdManufacturers").find({accessibleMenu:{$all:["retreatSafely"]}},{accessibleMenu:1})

{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba73e"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba73f"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba740"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba741"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba742"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba743"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba744"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba745"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba746"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba747"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba748"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba749"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba74a"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739000e3e867ed6ba74b"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba74c"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba74d"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba74e"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba74f"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba750"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba751"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba752"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba753"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba754"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba755"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba756"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba757"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba758"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba759"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba75a"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba75b"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba75c"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739100e3e867ed6ba75d"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba75e"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba75f"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba760"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba761"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba762"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba763"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba764"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba765"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba766"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba767"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba768"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba769"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba76a"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba76b"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba76c"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba76d"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba76e"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}
// ----------------------------------------------
{ 
    "_id" : ObjectId("5d36739200e3e867ed6ba76f"), 
    "accessibleMenu" : [
        "callCenter", 
        "mapSearch", 
        "album", 
        "helpCenter", 
        "serviceProtocol", 
        "taskCenter", 
        "voiceRobot", 
        "userCenter", 
        "userManagement", 
        "retreatSafely"
    ]
}

```

```
去除accessibleMenu数组特定值
单个：db.getCollection("ThirdManufacturers").update({"_id":ObjectId("5d36739000e3e867ed6ba73e")},{$pull:{accessibleMenu:{$in:["retreatSafely"]}}})、
全部：db.getCollection("ThirdManufacturers").updateMany({},{$pull:{accessibleMenu:{$in:["retreatSafely"]}}})

```







