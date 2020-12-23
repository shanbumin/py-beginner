#不可变集合


#Python中还有一种不可变类型的集合，名字叫frozenset。
#set跟frozenset的区别就如同list跟tuple的区别，frozenset由于是不可变类型，能够计算出哈希码，因此它可以作为set中的元素。
# 除了不能添加和删除元素，frozenset在其他方面跟set基本是一样的，下面的代码简单的展示了frozenset的用法。

set1 = frozenset({1, 3, 5, 7})
set2 = frozenset(range(1, 6))
print(set1 & set2)    # frozenset({1, 3, 5})
print(set1 | set2)    # frozenset({1, 2, 3, 4, 5, 7})
print(set1 - set2)    # frozenset({7})
print(set1 < set2)    # False