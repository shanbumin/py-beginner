#面向对象的编程语言支持在已有类的基础上创建新类，从而减少重复代码的编写。
#提供继承信息的类叫做父类（超类、基类），得到继承信息的类叫做子类（派生类、衍生类）。

#继承的语法是在定义类的时候，在类名后的圆括号中指定当前类的父类。
# 如果定义一个类的时候没有指定它的父类是谁，那么默认的父类是object类。
# object类是Python中的顶级类，这也就意味着所有的类都是它的子类，要么直接继承它，要么间接继承它。
# Python语言允许多重继承，也就是说一个类可以有一个或多个父类，
# 在子类的初始化方法中，我们可以通过super().__init__()来调用父类初始化方法，super函数是Python内置函数中专门为获取当前对象的父类对象而设计的。

class Person:
    """人类"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭.')

    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    """学生类"""

    def __init__(self, name, age):
        # super(Student, self).__init__(name, age)
        super().__init__(name, age)

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):
    """老师类"""

    def __init__(self, name, age, title):
        # super(Teacher, self).__init__(name, age)
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')


stu1 = Student('白元芳', 21)
stu2 = Student('狄仁杰', 22)
teacher = Teacher('武则天', 35, '副教授')
stu1.eat()
stu2.sleep()
teacher.teach('Python程序设计')
stu1.study('Python程序设计')

# todo 子类继承父类的方法后，还可以对方法进行重写（重新实现该方法），不同的子类可以对父类的同一个方法给出不同的实现版本，这样的方法在程序运行时就会表现出多态行为（调用相同的方法，做了不同的事情）。
#  多态是面向对象编程中最精髓的部分


