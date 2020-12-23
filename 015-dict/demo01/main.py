#Python程序中的字典跟现实生活中的字典很像，它以键值对（键和值的组合）的方式把数据组织到一起，我们可以通过键找到与之对应的值并进行操作。


#在Python中创建字典可以使用{}字面量语法，这一点跟集合是一样的。
# 但是字典的{}中的元素是以键值对的形式存在的，每个元素由:分隔的两个值构成，:前面是键，:后面是值，代码如下所示。

person = {
    'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号',
    'home': '中同仁路8号', 'tel': '13122334455', 'econtact': '13800998877'
}
print(person)


#当然，如果愿意，我们也可以使用内置函数dict或者是字典的生成式语法来创建字典，代码如下所示。


# dict函数(构造器)中的每一组参数就是字典中的一组键值对
person = dict(name='王大锤', age=55, weight=60, home='中同仁路8号')
print(person)    # {'name': '王大锤', 'age': 55, 'weight': 60, 'home': '中同仁路8号'}

# 可以通过Python内置函数zip压缩两个序列并创建字典
items1 = dict(zip('ABCDE', '12345'))
print(items1)    # {'A': '1', 'B': '2', 'C': '3', 'D': '4', 'E': '5'}
items2 = dict(zip('ABCDE', range(1, 10)))
print(items2)    # {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}

# 用字典生成式语法创建字典
items3 = {x: x ** 3 for x in range(1, 6)}
print(items3)     # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}


#想知道字典中一共有多少组键值对，仍然是使用len函数；如果想对字典进行遍历，可以用for循环，
# 但是需要注意，for循环只是对字典的键进行了遍历，不过没关系，在讲完字典的运算后，我们可以通过字典的键获取到和这个键对应的值。

person = {'name': '王大锤', 'age': 55, 'weight': 60, 'office': '科华北路62号'}
print(len(person))    # 4
for key in person:
    print(key)