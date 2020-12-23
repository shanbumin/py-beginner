# 元组的应用场景


#打包和解包操作。
# 打包
a = 1, 10, 100
print(type(a), a)    # <class 'tuple'> (1, 10, 100)
# 解包
i, j, k = a
print(i, j, k)       # 1 10 100

# 在解包时，如果解包出来的元素个数和变量个数不对应，会引发ValueError异
#有一种解决变量个数少于元素的个数方法，就是使用星号表达式，
# 我们之前讲函数的可变参数时使用过星号表达式。
# 有了星号表达式，我们就可以让一个变量接收多个值，代码如下所示。
# 需要注意的是，用星号表达式修饰的变量会变成一个列表，列表中有0个或多个元素。
# 还有在解包语法中，星号表达式只能出现一次。
a = 1, 10, 100, 1000
i, j, *k = a
print(i, j, k)          # 1 10 [100, 1000]
i, *j, k = a
print(i, j, k)          # 1 [10, 100] 1000
*i, j, k = a
print(i, j, k)          # [1, 10] 100 1000
*i, j = a
print(i, j)             # [1, 10, 100] 1000
i, *j = a
print(i, j)             # 1 [10, 100, 1000]
i, j, k, *l = a
print(i, j, k, l)       # 1 10 100 [1000]
i, j, k, l, *m = a
print(i, j, k, l, m)    # 1 10 100 1000 []


#需要说明一点，解包语法对所有的序列都成立，这就意味着对字符串、列表以及我们之前讲到的range函数返回的范围序列都可以使用解包语法。大家可以尝试运行下面的代码，看看会出现怎样的结果。

a, b, *c = range(1, 10)
print(a, b, c)
a, b, c = [1, 10, 100]
print(a, b, c)
a, *b, c = 'hello'
print(a, b, c)

