# 设计一个生成指定长度验证码的函数。

import random

ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


 # 生成指定长度的验证码
 # :param code_len: 验证码的长度(默认4个字符)
 # :return: 由大小写英文字母和数字构成的随机验证码字符串
def generate_code(code_len=4):
    code = ''
    for _ in range(code_len):
        index = random.randrange(0, len(ALL_CHARS))
        code += ALL_CHARS[index]
    return code



for _ in range(10):
    print(generate_code())






