# 高阶函数的用法
# 函数本身也可以作为函数的参数或返回值，这就是所谓的高阶函数。
import operator


#op是个函数类型
def calc(*args,op):
    result = 1
    for arg in args:
        result = op(result, arg)
    return result


def add(x,y):
    return x+y

def mul(x,y):
    return  x*y


print(calc(1,2,3,op=add))
print(calc(1,2,3,op=mul))

print('-'*100)
# 因为Python标准库中的operator模块提供了代表加法运算的add和代表乘法运算的mul函数，我们直接使用即可，代码如下所示。
print(calc(1,2,3,op=operator.add))
print(calc(1,2,3,op=operator.mul))
