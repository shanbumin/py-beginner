#在Python中，可以使用raise关键字来引发异常（抛出异常对象），而调用者可以通过try...except...结构来捕获并处理异常。
# 例如在函数中，当函数的执行条件不满足时，可以使用抛出异常的方式来告知调用者问题的所在，
# 而调用者可以通过捕获处理异常来使得代码从异常中恢复，定义异常和抛出异常的代码如下所示。




class InputError(ValueError):
    """自定义异常类型"""
    pass


def fac(num):
    """求阶乘"""
    if type(num) != int or num < 0:
        raise InputError('只能计算非负整数的阶乘！！！')
    if num in (0, 1):
        return 1
    return num * fac(num - 1)



# 调用求阶乘的函数fac，通过try...except...结构捕获输入错误的异常并打印异常对象（显示异常信息），如果输入正确就计算阶乘并结束程序。
flag = True
while flag:
    num = int(input('n = '))
    try:
        print(f'{num}! = {fac(num)}')
        flag = False
    except InputError as err:
        print(err)

