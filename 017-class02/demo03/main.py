#动态属性


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
# 为Student对象动态添加sex属性
stu.sex = '男'


#如果不希望在使用对象时动态的为对象添加属性，可以使用Python的__slots__魔法。
# 对于Student类来说，可以在类中指定__slots__ = ('name', 'age')，这样Student类的对象只能有name和age属性，如果想动态添加其他属性将会引发异常，代码如下所示。


class Student2:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student2('王大锤', 20)
# AttributeError: 'Student' object has no attribute 'sex'
#stu.sex = '男'