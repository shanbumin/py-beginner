#大家可能已经注意到了，刚才我们创建的学生对象只有行为没有属性，如果要给学生对象定义属性，我们可以修改Student类，为其添加一个名为__init__的方法。
# 在我们调用Student类的构造器创建对象时，首先会在内存中获得保存学生对象所需的内存空间，然后通过自动执行__init__方法，完成对内存的初始化操作，也就是把数据放到内存空间中。
# 所以我们可以通过给Student类添加__init__方法的方式为学生对象指定属性，同时完成对属性赋初始值的操作，正因如此，__init__方法通常也被称为初始化方法。



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




# 由于初始化方法除了self之外还有两个参数
# 所以调用Student类的构造器创建对象时要传入这两个参数
stu1 = Student('骆昊', 40)
stu2 = Student('王大锤', 15)
stu1.study('Python程序设计')    # 骆昊正在学习Python程序设计.
stu2.play()                    # 王大锤正在玩游戏.


