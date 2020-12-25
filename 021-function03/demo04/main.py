#Python中，使用装饰器很有更为便捷的语法糖,
#可以用@装饰器函数将装饰器函数直接放在被装饰的函数上，效果跟上面的代码相同，下面是完整的代码。

import random
import time


def record_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__}执行时间: {end - start:.3f}秒')
        return result

    return wrapper


@record_time
def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


@record_time
def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')


download('MySQL从删库到跑路.avi')
print("-"*100)
upload('Python从入门到住院.pdf')

#上面的代码，我们通过装饰器语法糖为download和upload函数添加了装饰器，这样调用download和upload函数时，会记录下函数的执行时间。
# 事实上，被装饰后的download和upload函数是我们在装饰器record_time中返回的wrapper函数，调用它们其实就是在调用wrapper函数，所以拥有了记录函数执行时间的功能。


