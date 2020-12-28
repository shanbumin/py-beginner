# 例子2：从一段文字中提取出国内手机号码


import re

# 创建正则表达式对象，使用了前瞻和回顾来保证手机号前后不应该再出现数字
sentence = '''重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
不是15600998765，也是110或119，王大锤的手机号才是15600998765。'''
pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')

# 方法一：查找所有匹配并保存到一个列表中 TODO:查找字符串所有与正则表达式匹配的模式 返回字符串的列表
tels_list = re.findall(pattern, sentence)
for tel in tels_list:
    print(tel)
print('--------华丽的分隔线--------')



# 方法二：通过迭代器取出匹配对象并获得匹配的内容 TODO:查找字符串所有与正则表达式匹配的模式 返回一个迭代器
for temp in pattern.finditer(sentence):
    print(temp.group())
print('--------华丽的分隔线--------')

# 方法三：通过search函数指定搜索位置找出所有匹配  TODO:搜索字符串中第一次出现正则表达式的模式 成功返回匹配对象 否则返回None
m = pattern.search(sentence)
while m:
    print(m.group())
    m = pattern.search(sentence, m.end())


