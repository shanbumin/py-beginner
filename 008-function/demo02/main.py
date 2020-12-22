# 参数的默认值


def test(n=2):
    return n+1


print(test())
print(test(3))
print("-----------------------------------------------------------")

def add(a=0, b=0, c=0):
    return a + b + c


print(add())         # 0 调用add函数，没有传入参数，那么a、b、c都使用默认值0
print(add(1))        # 1 调用add函数，传入一个参数，那么该参数赋值给变量a, 变量b和c使用默认值0
print(add(1, 2))     # 3 调用add函数，传入两个参数，1和2分别赋值给变量a和b，变量c使用默认值0
print(add(1, 2, 3))  # 6 调用add函数，传入三个参数，分别赋值给a、b、c三个变量
print(add(c=50, a=100, b=200))   # 350 传递参数时可以不按照设定的顺序进行传递，但是要用“参数名=参数值”的形式



#todo 注意：带默认值的参数必须放在不带默认值的参数之后，否则将产生SyntaxError错误，
# 错误消息是：non-default argument follows default argument，翻译成中文的意思是“没有默认值的参数放在了带默认值的参数后面”。