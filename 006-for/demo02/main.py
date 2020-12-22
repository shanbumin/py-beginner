
#如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环。while循环通过一个能够产生或转换出bool值的表达式来控制循环，表达式的值为True则继续循环；表达式的值为False则结束循环。

import  random

# 产生一个1-100范围的随机数

answer = random.randint(1,100)
counter =0
while True:
    counter += 1
    number = int(input('请输入:'))
    if number <answer:
        print('大一点')
    elif number>answer:
        print('小一点')
    else:
        print('恭喜你猜对了!')
        break

# 当退出while循环的时候显示用户一共猜了多少次
print(f'你总共猜了{counter}次')