


"""
输入两个正整数计算它们的最大公约数和最小公倍数
提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
#两个数的乘积等于这两个数的最大公约数与最小公倍数的乘积。假设有两个数是a、b，它们的最大公约数是p，最小公倍数是q。那么有这样的关系：ab=pq。”
"""

#todo 首先保证y大于x
x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x    # Python中可以用这样的方式来交换两个变量的值
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(f'{x}和{y}的最大公约数是{factor}')
        print(f'{x}和{y}的最小公倍数是{x * y // factor}')
        break


