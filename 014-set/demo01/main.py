# 创建集合可以使用{}字面量语法，{}中需要至少有一个元素，因为没有元素的{}并不是空集合而是一个空字典，要创建空集合可以使用set()；
# 当然，也可以使用内置函数set来创建一个集合，准确的说set并不是一个函数，而是创建集合对象的构造器。
# 也可以将其他序列转换成集合，例如：set('hello')会得到一个包含了4个字符的集合（重复的l会被去掉）。
# 除了这两种方式，我们还可以使用生成式语法来创建集合，就像我们之前用生成式创建列表那样。
# 要知道集合中有多少个元素，还是使用内置函数len；
# 使用for循环可以实现对集合元素的遍历。


# 创建集合的字面量语法(重复元素不会出现在集合中)
set1 = {1, 2, 3, 3, 3, 2}
print(set1)         # {1, 2, 3}
print(len(set1))    # 3

# 创建集合的构造器语法(后面会讲到什么是构造器)
set2 = set('hello')
print(set2)         # {'h', 'l', 'o', 'e'}



# 将列表转换成集合(可以去掉列表中的重复元素)
set3 = set([1, 2, 3, 3, 2, 1])
print(set3)         # {1, 2, 3}

# 创建集合的生成式语法(将列表生成式的[]换成{})
set4 = {num for num in range(1, 20) if num % 3 == 0 or num % 5 == 0}
print(set4)         # {3, 5, 6, 9, 10, 12, 15, 18}

# 集合元素的循环遍历
for elem in set4:
    print(elem)





#需要提醒大家，集合中的元素必须是hashable类型。所谓hashable类型指的是能够计算出哈希码的数据类型，
# 你可以暂时将哈希码理解为和变量对应的唯一的ID值。
# 通常不可变类型都是hashable类型，如整数、浮点、字符串、元组等，而可变类型都不是hashable类型，因为可变类型无法确定唯一的ID值，所以也就不能放到集合中。
# 集合本身也是可变类型，所以集合不能够作为集合中的元素，这一点请大家一定要注意。