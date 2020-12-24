
#在Python中，可以通过给对象属性名添加前缀下划线的方式来说明属性的访问可见性，
#例如，可以用__name表示一个私有属性，_name表示一个受保护属性，代码如下所示。

class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def study(self, course_name):
        print(f'{self.__name}正在学习{course_name}.')


stu = Student('王大锤', 20)
stu.study('Python程序设计')
#print(stu.__name) #__name是私有的，在类的外面无法直接访问，但是类里面的study方法中可以通过self.__name访问该属性。





#需要提醒大家的是，Python并没有从语法上严格保证私有属性的私密性，它只是给私有的属性和方法换了一个名字来阻挠对它们的访问，
# 事实上如果你更换名字的规则仍然可以访问到它们，我们可以对上面的代码稍作修改就可以访问到私有的。


stu = Student('王大锤', 20)
stu.study('Python程序设计')
print(stu._Student__name, stu._Student__age)

#Python中做出这样的设定是基于一句名言：“We are all consenting adults here”（大家都是成年人）。
#Python语言的设计者认为程序员要为自己的行为负责，而不是由Python语言本身来严格限制访问可见性，而大多数的程序员都认为开放比封闭要好，把对象的属性私有化并不是必须的东西。

