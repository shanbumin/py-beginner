import random
import time

from functools import wraps

# 如果希望取消装饰器的作用，那么在定义装饰器函数的时候，需要做一些额外的工作。
# Python标准库functools模块的wraps函数也是一个装饰器，我们将它放在wrapper函数上，这个装饰器可以帮我们保留被装饰之前的函数，这样在需要取消装饰器时，
# 可以通过被装饰函数的__wrapped__属性获得被装饰之前的函数。
def record_time(func):
    #这里是用来支持外部取消装饰器的额
    @wraps(func)
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
upload('Python从入门到住院.pdf')
print("-"*100)
# 取消装饰器
download.__wrapped__('MySQL必知必会.pdf')  #该属性值就是装饰前的函数
upload = upload.__wrapped__
upload('Python从新手到大师.pdf')
