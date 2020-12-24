
#我们之前讲过在函数的参数列表中可以使用可变参数*args来接收任意数量的参数，但是我们需要看看，*args是否能够接收带参数名的参数。


def calc(*args):
    result = 0
    for arg in args:
        result += arg
    return result


#todo 执行代码会引发TypeError错误，错误消息为calc() got an unexpected keyword argument 'a'，由此可见，*args并不能处理带参数名的参数。
#print(calc(a=1, b=2, c=3))



#我们在设计函数时，如果既不知道调用者会传入的参数个数，也不知道调用者会不会指定参数名，那么同时使用可变参数和关键字参数。
# todo [关键字参数]会将传入的带参数名的参数组装成一个字典，参数名就是字典中键值对的键，而参数值就是字典中键值对的值，代码如下所示。
# todo 提示：不带参数名的参数（位置参数）必须出现在带参数名的参数（关键字参数）之前，否则将会引发异常。
def calc2(*args, **kwargs):
    result = 0
    for arg in args:
        result += arg
    for value in kwargs.values():
        result += value
    return result


print(calc2())                  # 0
print(calc2(1, 2, 3))           # 6
print(calc2(a=1, b=2, c=3))     # 6
print(calc2(1, 2, c=3, d=4))    # 10