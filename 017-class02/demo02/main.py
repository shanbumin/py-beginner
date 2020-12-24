# Python中可以通过property装饰器为“私有”属性提供读取和修改的方法，装饰器通常会放在类、函数或方法的声明之前，通过一个@符号表示将装饰器应用于类、函数或方法。
# 装饰器的概念我们会在稍后的课程中以专题的形式为大家讲解，这里我们只需要了解property装饰器的用法就可以了。
# todo 类似  getter 和 setter



class Student:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # 属性访问器(getter方法) - 获取__name属性
    @property
    def name(self):
        return self.__name

    # 属性修改器(setter方法) - 修改__name属性
    @name.setter
    def name(self, name):
        # 如果name参数不为空就赋值给对象的__name属性
        # 否则将__name属性赋值为'无名氏'，有两种写法
        # self.__name = name if name else '无名氏'
        self.__name = name or '无名氏'

    @property
    def age(self):
        return self.__age


stu = Student('王大锤', 20)
print(stu.name, stu.age)  # 王大锤 20  stu.name默认没有该属性的时候，会触发属性获取访问器，类似php中的魔方方法啦
stu.name = ''
print(stu.name)  # 无名氏
# stu.age = 30     # AttributeError: can't set attribute
# 在实际项目开发中，我们并不经常使用私有属性，属性装饰器的使用也比较少，所以上面的知识点大家简单了解一下就可以了。