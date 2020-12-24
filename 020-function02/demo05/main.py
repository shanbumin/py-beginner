


def is_even(num):
    return num % 2 == 0


def square(num):
    return num ** 2


numbers1 = [35, 12, 8, 99, 60, 52]

#对numbers1中的所有元素使用is_even进行过滤，之后将符合的元素进行square处理
numbers2 = list(map(square, filter(is_even, numbers1)))
print(numbers2)    # [144, 64, 3600, 2704]



# 当然，要完成上面代码的功能，也可以使用列表生成式，列表生成式的做法更为简单优雅。
numbers1 = [35, 12, 8, 99, 60, 52]
numbers2 = [num ** 2 for num in numbers1 if num % 2 == 0]
print(numbers2)    # [144, 64, 3600, 2704]
