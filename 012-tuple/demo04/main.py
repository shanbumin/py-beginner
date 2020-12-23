

#现在我们可以反过来思考一下函数的可变参数，可变参数其实就是将多个参数打包成了一个元组，可以通过下面的代码来证明这一点。


def add(*args):
    print(type(args), args)
    total = 0
    for val in args:
        total += val
    return total


add(1, 10, 20)        # <class 'tuple'> (1, 10, 20)
add(1, 2, 3, 4, 5)    # <class 'tuple'> (1, 2, 3, 4, 5)