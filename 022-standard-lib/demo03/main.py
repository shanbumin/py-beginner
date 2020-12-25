#使用namedtuple创建扑克牌类的例子
#namedtuple：命令元组，它是一个类工厂，接受类型的名称和属性列表来创建一个类。

from collections import namedtuple

Card = namedtuple('Card', ('suite', 'face'))
card1 = Card('红桃', 5)
card2 = Card('草花', 9)


print(f'{card1.suite}{card1.face}')
print(f'{card2.suite}{card2.face}')
