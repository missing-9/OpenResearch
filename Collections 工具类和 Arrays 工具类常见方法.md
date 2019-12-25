Collections 工具类和 Arrays 工具类常见方法

Collections

void reverse(List list)//反转
void shuffle(List list)//随机排序
void sort(List list)//按自然排序的升序排序
void sort(List list, Comparator c)//定制排序，由Comparator控制排序逻辑
void swap(List list, int i , int j)//交换两个索引位置的元素
void rotate(List list, int distance)//旋转。当distance为正数时，将list后distance个元素整体移到前面。当distance为负数时，将 list的前distance个元素整体移到后面。

int binarySearch(List list, Object key)//对List进行二分查找，返回索引，注意List必须是有序的
int max(Collection coll)//根据元素的自然顺序，返回最大的元素。 类比int min(Collection coll)
int max(Collection coll, Comparator c)//根据定制排序，返回最大元素，排序规则由Comparatator类控制。类比int min(Collection coll, Comparator c)
void fill(List list, Object obj)//用指定的元素代替指定list中的所有元素。
int frequency(Collection c, Object o)//统计元素出现次数
int indexOfSubList(List list, List target)//统计target在list中第一次出现的索引，找不到则返回-1，类比int lastIndexOfSubList(List source, list target).
boolean replaceAll(List list, Object oldVal, Object newVal), 用新元素替换旧元素

同步控制

Collections提供了多个synchronizedXxx()方法·，该方法可以将指定集合包装成线程同步的集合，从而解决多线程并发访问集合时的线程安全问题。

HashSet，TreeSet，ArrayList,LinkedList,HashMap,TreeMap 都是线程不安全的。Collections提供了多个静态方法可以把他们包装成线程同步的集合。

最好不要用下面这些方法，效率非常低，需要线程安全的集合类型时请考虑使用 JUC 包下的并发集合。
synchronizedCollection(Collection<T>  c) //返回指定 collection 支持的同步（线程安全的）collection。
synchronizedList(List<T> list)//返回指定列表支持的同步（线程安全的）List。
synchronizedMap(Map<K,V> m) //返回由指定映射支持的同步（线程安全的）Map。
synchronizedSet(Set<T> s) //返回指定 set 支持的同步（线程安全的）set。

Collections还可以设置不可变集合，提供了如下三类方法：
emptyXxx(): 返回一个空的、不可变的集合对象，此处的集合既可以是List，也可以是Set，还可以是Map。
singletonXxx(): 返回一个只包含指定对象（只有一个或一个元素）的不可变的集合对象，此处的集合可以是：List，Set，Map。
unmodifiableXxx(): 返回指定集合对象的不可变视图，此处的集合可以是：List，Set，Map。
上面三类方法的参数是原有的集合对象，返回值是该集合的”只读“版本。

//Collections.emptyXXX();创建一个空的、不可改变的XXX对象
List<Object> list = Collections.emptyList();
System.out.println(list);//[]
Set<Object> objects = Collections.emptySet();
System.out.println(objects);//[]
Map<Object, Object> objectObjectMap = Collections.emptyMap();
System.out.println(objectObjectMap);//{}

//Collections.singletonXXX();
List<ArrayList<Integer>> arrayLists = Collections.singletonList(arrayList);
System.out.println(arrayLists);//[[-1, 3, 3, -5, 7, 4, -9, -7]]
//创建一个只有一个元素，且不可改变的Set对象
Set<ArrayList<Integer>> singleton = Collections.singleton(arrayList);
System.out.println(singleton);//[[-1, 3, 3, -5, 7, 4, -9, -7]]
Map<String, String> nihao = Collections.singletonMap("1", "nihao");
System.out.println(nihao);//{1=nihao}

//unmodifiableXXX();创建普通XXX对象对应的不可变版本
List<Integer> integers = Collections.unmodifiableList(arrayList);
System.out.println(integers);//[-1, 3, 3, -5, 7, 4, -9, -7]
Set<Integer> integers2 = Collections.unmodifiableSet(integers1);
System.out.println(integers2);//[1, 2, 3]
Map<Object, Object> objectObjectMap2 = Collections.unmodifiableMap(scores);
System.out.println(objectObjectMap2);//{Java=82, 语文=80}

//添加出现异常：java.lang.UnsupportedOperationException
//        list.add(1);
//        arrayLists.add(arrayList);
//        integers.add(1);

Arrays类的常见操作
排序 : sort()
查找 : binarySearch()
比较: equals()
填充 : fill()
转列表: asList()
转字符串 : toString()
复制: copyOf()


参考链接：https://gitee.com/SnailClimb/JavaGuide/blob/master/docs/java/Basis/Arrays,CollectionsCommonMethods.md#collections