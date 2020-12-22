

"""
输入一个正整数判断它是不是素数
提示：素数指的是只能被1和自身整除的大于1的整数。
1.先假设x其是素数
2.将2,3,4... x ** 0.5分别来整除x，只要有一个可以，则x就不是素数啦

"""
num = int(input('请输入一个正整数: '))
end = int(num ** 0.5)
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')



