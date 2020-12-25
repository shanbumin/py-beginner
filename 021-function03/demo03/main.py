#重复的代码是万恶之源，那么有没有办法在不写重复代码的前提下，用一种简单优雅的方式记录下函数的执行时间呢？
# 在Python中，装饰器就是解决这类问题的最佳选择。
# 我们可以把记录函数执行时间的功能封装到一个装饰器中，在有需要的地方直接使用这个装饰器就可以了，代码如下所示。


import time
import random


def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')


# 定义装饰器函数，它的参数是被装饰的函数或类
def record_time(func):
    # 定义一个带装饰功能（记录被装饰函数的执行时间）的函数
    # 因为不知道被装饰的函数有怎样的参数所以使用*args和**kwargs接收所有参数
    # todo 在Python中函数可以嵌套的定义（函数中可以再定义函数）
    def wrapper(*args, **kwargs):
        # 在执行被装饰的函数之前记录开始时间
        start = time.time()
        # 执行被装饰的函数并获取返回值
        result = func(*args, **kwargs)
        # 在执行被装饰的函数之后记录结束时间
        end = time.time()
        # 计算和显示被装饰函数的执行时间
        print(f'{func.__name__}执行时间: {end - start:.3f}秒')
        # 返回被装饰函数的返回值（装饰器通常不会改变被装饰函数的执行结果）
        return result

    # 返回带装饰功能的wrapper函数
    return wrapper



# 使用上面的装饰器函数有两种方式，第一种方式就是直接调用装饰器函数，传入被装饰的函数并获得返回值，
# 我们可以用这个返回值直接覆盖原来的函数，那么在调用时就已经获得了装饰器提供的额外的功能（记录执行时间），大家可以试试下面的代码就明白了。


download = record_time(download)
upload = record_time(upload)
download('MySQL从删库到跑路.avi')
print("-"*100)
upload('Python从入门到住院.pdf')

