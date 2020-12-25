import time
from functools import wraps
import  random

# 装饰器函数本身也可以参数化，简单的说就是通过我们的装饰器也是可以通过调用者传入的参数来定制的，这个知识点我们在后面用上它的时候再为大家讲解。
# 除了可以用函数来定义装饰器之外，通过定义类的方式也可以定义装饰器。
# 如果一个类中有名为__call__的魔术方法，那么这个类的对象就可以像函数一样调用，这就意味着这个对象可以像装饰器一样工作，代码如下所示。
class RecordTime:

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f'{func.__name__}执行时间: {end - start:.3f}秒')
            return result

        return wrapper


# 使用装饰器语法糖添加装饰器
@RecordTime()
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')


# 直接创建对象并调用对象传入被装饰的函数
upload = RecordTime()(upload)
upload('Python从入门到住院.pdf')
print("-"*100)
download('MySQL从删库到跑路.avi')


#上面的代码演示了两种添加装饰器的方式，由于RecordTime是一个类，所以需要先创建对象，才能把对象当成装饰器来使用，
# 所以提醒大家注意RecordTime后面的圆括号，那是调用构造器创建对象的语法。
# 如果为RecordTime类添加一个__init__方法，就可以实现对装饰器的参数化，
# 刚才我们说过了，这个知识点等用上的时候再为大家讲解。
# 使用装饰器还可以装饰一个类，为其提供额外的功能，这个知识点也等我们用到的时候再做讲解。

