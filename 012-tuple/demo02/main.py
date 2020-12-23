#一个元组中如果有两个元素，我们就称之为二元组；一个元组中如果五个元素，我们就称之为五元组。
# 需要提醒大家注意的是，()表示空元组，但是如果元组中只有一个元素，需要加上一个逗号，否则()就不是代表元组的字面量语法，而是改变运算优先级的圆括号，
# 所以('hello', )和(100, )才是一元组，而('hello')和(100)只是字符串和整数。



# 空元组
a = ()
print(type(a))    # <class 'tuple'>
# 不是元组
b = ('hello')
print(type(b))    # <class 'str'>
c = (100)
print(type(c))    # <class 'int'>
# 一元组
d = ('hello', )
print(type(d))    # <class 'tuple'>
e = (100, )
print(type(e))    # <class 'tuple'>
