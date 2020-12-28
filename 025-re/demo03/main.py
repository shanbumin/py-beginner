# 例子3：替换字符串中的不良内容
import re

sentence = 'Oh, shit! 你丫是傻叉吗? Fuck you.'
# todo 用指定的字符串替换原字符串中与正则表达式匹配的模式 可以用count指定替换的次数
purified = re.sub('fuck|shit|[傻煞沙]','*', sentence, flags=re.IGNORECASE)
print(purified)  # Oh, *! 你丫是*吗? * you.


