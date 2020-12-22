"""
比较运算符(关系运算符)==、!=、<、>、<=、>=
和逻辑运算符的使用 and、or和not

Version: 0.1
"""
flag0 = 1 == 1 # True
flag1 = 3 > 2  # True
flag2 = 2 < 1  # False
flag3 = flag1 and flag2   # False
flag4 = flag1 or flag2   # True
flag5 = not (1 != 2)     # False
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False


# todo 比较运算符的优先级高于赋值运算符，所以flag0 = 1 == 1先做1 == 1产生布尔值True，再将这个值赋值给变量flag0。

