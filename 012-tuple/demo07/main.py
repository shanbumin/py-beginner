#Python中已经有了列表类型，为什么还需要元组这样的类型呢？

#1.元组是不可变类型，不可变类型更适合多线程环境，因为它降低了并发访问变量的同步化开销。关于这一点，我们会在后面讲解多线程的时候为大家详细论述。
#2.元组是不可变类型，通常不可变类型在创建时间和占用空间上面都优于对应的可变类型。我们可以使用sys模块的getsizeof函数来检查保存相同元素的元组和列表各自占用了多少内存空间。
# 我们也可以使用timeit模块的timeit函数来看看创建保存相同元素的元组和列表各自花费的时间，代码如下所示。


import sys
import timeit

a = list(range(100000))
b = tuple(range(100000))
print(sys.getsizeof(a), sys.getsizeof(b))    # 900120 800056

print(timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]'))
print(timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)'))