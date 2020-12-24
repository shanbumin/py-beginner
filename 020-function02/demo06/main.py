#匿名函数



# 比方说，我要写一个函数用于两个数相乘
#如果用def方式来写：
def mul(x,y):
    return  x*y

print(mul(2,3))
#用匿名函数来写：


var001=lambda x,y:x*y
print(var001(2,4))


#那么，匿名函数的优点是什么呢？

# 不用取名称，因为给函数取名是比较头疼的一件事，特别是函数比较多的时候
# 可以直接在使用的地方定义，如果需要修改，直接找到修改即可，方便以后代码的维护工作
# 语法结构简单，不用使用def 函数名(参数名):这种方式定义，直接使用lambda 参数:返回值 定义即可
