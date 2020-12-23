#------------------------添加和删除元素--------------------------------------------


items = ['Python', 'Java', 'Go', 'Kotlin']

# 使用append方法在列表尾部添加元素
items.append('Swift')
print(items)    # ['Python', 'Java', 'Go', 'Kotlin', 'Swift']


# 使用insert方法在列表指定索引位置插入元素
items.insert(2, 'SQL')
print(items)    # ['Python', 'Java', 'SQL', 'Go', 'Kotlin', 'Swift']

# 删除指定的元素
items.remove('Java')
print(items)    # ['Python', 'SQL', 'Go', 'Kotlin', 'Swift']



# 删除指定索引位置的元素
items.pop(0)
items.pop(len(items) - 1)
print(items)    # ['SQL', 'Go', 'Kotlin']

# 清空列表中的元素
items.clear()
print(items)    # []


#需要提醒大家，在使用remove方法删除元素时，如果要删除的元素并不在列表中，会引发ValueError异常，错误消息是：list.remove(x): x not in list。
# 在使用pop方法删除元素时，如果索引的值超出了范围，会引发IndexError异常，错误消息是：pop index out of range。
#从列表中删除元素其实还有一种方式，就是使用Python中的del关键字后面跟要删除的元素，
# 这种做法跟使用pop方法指定索引删除元素没有实质性的区别，但后者会返回删除的元素，
# 前者在性能上略优（del对应字节码指令是DELETE_SUBSCR，而pop对应的字节码指令是CALL_METHOD和POP_TOP）。

items = ['Python', 'Java', 'Go', 'Kotlin']
del items[1]
print(items)    # ['Python', 'Go', 'Kotlin']


#-------------------------------------------元素位置和次数----------------------------------------------------------------

items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']

# 查找元素的索引位置
print(items.index('Python'))       # 0
print(items.index('Python', 2))    # 5
# 注意：虽然列表中有'Java'，但是从索引为3这个位置开始后面是没有'Java'的
#print(items.index('Java', 3))      # ValueError: 'Java' is not in list


items = ['Python', 'Java', 'Java', 'Go', 'Kotlin', 'Python']

# 查找元素出现的次数
print(items.count('Python'))    # 2
print(items.count('Go'))        # 1
print(items.count('Swfit'))     # 0


#-------------------------------------------元素排序和反转----------------------------------------------------------------
items = ['Python', 'Java', 'Go', 'Kotlin', 'Python']

# 排序
items.sort()
print(items)    # ['Go', 'Java', 'Kotlin', 'Python', 'Python']
# 反转
items.reverse()
print(items)    # ['Python', 'Python', 'Kotlin', 'Java', 'Go']



























