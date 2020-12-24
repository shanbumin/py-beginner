


#调用函数时，如果希望函数的调用者必须以参数名=参数值的方式传参，可以用命名关键字参数取代位置参数。
# 所谓命名关键字参数，是在函数的参数列表中，写在*之后的参数，代码如下所示。


def can_form_triangle(*, a, b, c):
    print(f'a = {a}, b = {b}, c = {c}')
    return a + b > c and b + c > a and a + c > b


# TypeError: can_form_triangle() takes 0 positional arguments but 3 were given
# print(is_valid_for_triangle(3, 4, 5))



# 传参时必须使用“参数名=参数值”的方式，位置不重要
print(can_form_triangle(a=3, b=4, c=5))
print(can_form_triangle(c=5, b=4, a=3))


#todo 注意：上面的can_form_triangle函数，参数列表中的*是一个分隔符，*前面的参数都是位置参数，而*后面的参数就是命名关键字参数。

