# 打印对象
#上面我们通过__init__方法在创建对象时为对象绑定了属性并赋予了初始值。
# 在Python中，以两个下划线__（读作“dunder”）开头和结尾的方法通常都是有特殊用途和意义的方法，我们一般称之为魔术方法或魔法方法。
# 如果我们在打印对象的时候不希望看到对象的地址而是看到我们自定义的信息，可以通过在类中放置__repr__魔术方法来做到，该方法返回的字符串就是用print函数打印对象的时候会显示的内容，代码如下所示。


class Student:
    """学生"""

    def __init__(self, name, age):
        """初始化方法"""
        self.name = name
        self.age = age

    def study(self, course_name):
        """学习"""
        print(f'{self.name}正在学习{course_name}.')

    def play(self):
        """玩耍"""
        print(f'{self.name}正在玩游戏.')

    def __repr__(self):
        return f'{self.name}: {self.age}'


stu1 = Student('骆昊', 40)
print(stu1)        # 骆昊: 40
students = [stu1, Student('王小锤', 16), Student('王大锤', 25)]
print(students)    # [骆昊: 40, 王小锤: 16, 王大锤: 25]





