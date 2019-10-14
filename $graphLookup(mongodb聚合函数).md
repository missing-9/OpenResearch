# $graphLookup(聚合函数)

一、定义

$graphLookup 是一种集合递归查询方式，严格限制查询深度和查询过滤条件。

1，在文档中输入$graphLookup 开始聚合查询。

2，关键字from是$graphLookup 要查询的集合。

3，对于每次输入的文档，查询都会从startWith 关键字开始

4，$graphLookup将集合中其他的connectField值与startWith相匹配。

5，对于每次匹配的文档，$graphLookup会先拿到connectFromField的值，在from标志的集合中查找能和connectToField匹配的文档。对于每次匹配，$graphLookup会将文档添加到以as关键字命名的数组。

递归循环这些步骤直到找不到匹配的文档，或者操作数量达到以maxDepth关键字关键字的深度。$graphLookup将数据连接到输入的文档上。搜索完集合中全部文档后$graphLookup返回搜索结果。

二、$graphLookup示例形式

```s
{
   $graphLookup: {
      from: <collection>,
      startWith: <expression>,
      connectFromField: <string>,
      connectToField: <string>,
      as: <string>,
      maxDepth: <number>,
      depthField: <string>,
      restrictSearchWithMatch: <document>
   }
}
```
三、举例

```
集合：
{ "_id" : 1, "name" : "Dev" }
{ "_id" : 2, "name" : "Eliot", "reportsTo" : "Dev" }
{ "_id" : 3, "name" : "Ron", "reportsTo" : "Eliot" }
{ "_id" : 4, "name" : "Andrew", "reportsTo" : "Eliot" }
{ "_id" : 5, "name" : "Asya", "reportsTo" : "Ron" }
{ "_id" : 6, "name" : "Dan", "reportsTo" : "Andrew" }
```
```
 聚合函数：
db.employees.aggregate( [
   {
      $graphLookup: {
         from: "employees",
         startWith: "$reportsTo",
         connectFromField: "reportsTo",
         connectToField: "name",
         as: "reportingHierarchy"
      }
   }
] )
```
```
返回结果：
{
   "_id" : 1,
   "name" : "Dev",
   "reportingHierarchy" : [ ]
}
{
   "_id" : 2,
   "name" : "Eliot",
   "reportsTo" : "Dev",
   "reportingHierarchy" : [
      { "_id" : 1, "name" : "Dev" }
   ]
}
{
   "_id" : 3,
   "name" : "Ron",
   "reportsTo" : "Eliot",
   "reportingHierarchy" : [
      { "_id" : 1, "name" : "Dev" },
      { "_id" : 2, "name" : "Eliot", "reportsTo" : "Dev" }
   ]
}
{
   "_id" : 4,
   "name" : "Andrew",
   "reportsTo" : "Eliot",
   "reportingHierarchy" : [
      { "_id" : 1, "name" : "Dev" },
      { "_id" : 2, "name" : "Eliot", "reportsTo" : "Dev" }
   ]
}
{
   "_id" : 5,
   "name" : "Asya",
   "reportsTo" : "Ron",
   "reportingHierarchy" : [
      { "_id" : 1, "name" : "Dev" },
      { "_id" : 2, "name" : "Eliot", "reportsTo" : "Dev" },
      { "_id" : 3, "name" : "Ron", "reportsTo" : "Eliot" }
   ]
}
{
   "_id" : 6,
   "name" : "Dan",
   "reportsTo" : "Andrew",
   "reportingHierarchy" : [
      { "_id" : 1, "name" : "Dev" },
      { "_id" : 2, "name" : "Eliot", "reportsTo" : "Dev" },
      { "_id" : 4, "name" : "Andrew", "reportsTo" : "Eliot" }
   ]
}
```