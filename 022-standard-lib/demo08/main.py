#itertools可以帮助我们生成各种各样的迭代器，大家可以看看下面的例子。

import itertools
import time

#todo  permutations  [ˌpɜːmju(ː)ˈteɪʃənz]  n.排列(方式);组合(方式);置换


# 产生ABCD的全排列
for value in itertools.permutations('ABCD'):
    print(value)

print("-"*100)

# 产生ABCDE的五选三组合
for value in itertools.combinations('ABCDE', 3):
    print(value)

print("-"*100)


# # 产生ABCD和123的笛卡尔积
for value in itertools.product('ABCD', '123'):
    print(value)

print("-"*100)


# 产生ABC的无限循环序列
it = itertools.cycle(('A', 'B', 'C'))

while True:
  print(next(it))
  time.sleep(1)
  print("*"*10)



