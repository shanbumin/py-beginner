
#定义类
# 在Python中，可以使用class关键字加上类名来定义类，通过缩进我们可以确定类的代码块，就如同定义函数那样。
# 在类的代码块中，我们需要写一些函数，我们说过类是一个抽象概念，那么这些函数就是我们对一类对象共同的动态特征的提取。
# 写在类里面的函数我们通常称之为方法，方法就是对象的行为，也就是对象可以接收的消息。
# 方法的第一个参数通常都是self，它代表了接收这个消息的对象本身。

class  Student:

    def study(self,course_name):
        print(f'学生正在学习{course_name}.')

    def play(self):
        print(f'学生正在玩游戏.')


#在我们定义好一个类之后，可以使用构造器语法来创建对象，代码如下所示。
stu1 = Student()
stu2 = Student()
print(stu1)    # <__main__.Student object at 0x10ad5ac50>
print(stu2)    # <__main__.Student object at 0x10ad5acd0>
print(hex(id(stu1)), hex(id(stu2)))    # 0x10ad5ac50 0x10ad5acd0



# 通过“类.方法”调用方法，第一个参数是接收消息的对象，第二个参数是学习的课程名称
Student.study(stu1, 'Python程序设计')    # 学生正在学习Python程序设计.
# 通过“对象.方法”调用方法，点前面的对象就是接收消息的对象，只需要传入第二个参数
stu1.study('Python程序设计')             # 学生正在学习Python程序设计.

Student.play(stu2)    # 学生正在玩游戏.
stu2.play()           # 学生正在玩游戏.
