# 静态方法和类方法

# 之前我们在类中定义的方法都是对象方法，换句话说这些方法都是对象可以接收的消息。
# 除了对象方法之外，类中还可以有静态方法和类方法，这两类方法是发给类的消息，二者并没有实质性的区别。
# 在面向对象的世界里，一切皆为对象，我们定义的每一个类其实也是一个对象，而静态方法和类方法就是发送给类对象的消息。
# todo 那么，什么样的消息会直接发送给类对象呢？
#  在调用某个方法时对象还没有创建出来。我们可以把这类方法设计为静态方法或类方法，也就是说这类方法不是发送给对象的消息，而是发送给的消息，代码如下所示。


class Triangle(object):
    """三角形类"""

    def __init__(self, a, b, c):
        """初始化方法"""
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        """判断三条边长能否构成三角形(静态方法)"""
        return a + b > c and b + c > a and a + c > b

    @classmethod
    def is_valid2(cls, a, b, c):
        """判断三条边长能否构成三角形(类方法)"""
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        """计算周长"""
        return self.a + self.b + self.c

    def area(self):
        """计算面积"""
        p = self.perimeter() / 2
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5


# 上面的代码使用staticmethod装饰器声明了is_valid方法是Triangle类的静态方法，
# 如果要声明类方法，可以使用classmethod装饰器。如is_valid2
# 可以直接使用类名.方法名的方式来调用静态方法和类方法，二者的区别在于，类方法的第一个参数是类对象本身，而静态方法则没有这个参数。
# 简单的总结一下，对象方法、类方法、静态方法都可以通过类名.方法名的方式来调用，区别在于方法的第一个参数到底是普通对象还是类对象，还是没有接受消息的对象。
# 静态方法通常也可以直接写成一个独立的函数，因为它并没有跟特定的对象绑定。






