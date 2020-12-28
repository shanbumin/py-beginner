#例子4：拆分长字符串
import re

#用正则表达式指定的模式分隔符拆分字符串 返回列表
poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
sentences_list = re.split(r'[，。, .]', poem)
sentences_list = [sentence for sentence in sentences_list if sentence]
for sentence in sentences_list:
    print(sentence)
