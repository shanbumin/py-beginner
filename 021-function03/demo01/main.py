#假设已经有名为downlaod和upload的两个函数，分别用于文件的上传和下载，
import random
import time


def download(filename):
    print(f'开始下载{filename}.')
    time.sleep(random.randint(2, 6))
    print(f'{filename}下载完成.')


def upload(filename):
    print(f'开始上传{filename}.')
    time.sleep(random.randint(4, 8))
    print(f'{filename}上传完成.')


download('MySQL从删库到跑路.avi')
print('-'*100)
upload('Python从入门到住院.pdf')