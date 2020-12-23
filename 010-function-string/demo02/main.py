import random
import string

ALL_CHARS = string.digits + string.ascii_letters


def generate_code(code_len=4):
    return ''.join(random.choices(ALL_CHARS, k=code_len))


print(generate_code(10))


#说明：random模块的sample和choices函数都可以实现随机抽样，sample实现无放回抽样，这意味着抽样取出的字符是不重复的；
# choices实现有放回抽样，这意味着可能会重复选中某些字符。这两个函数的第一个参数代表抽样的总体，而参数k代表抽样的数量