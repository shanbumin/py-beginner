# 例如我们之前讲到的阶乘，非负整数N的阶乘是N乘以N - 1 的阶乘，即N! = N * (N - 1)!，
# 定义的左边和右边都出现了阶乘的概念，所以这是一个递归定义。
# 既然如此，我们可以使用递归调用的方式来写一个求阶乘的函数，代码如下所示。

def fac(num):
    if num in (0, 1):
        return 1
    return num * fac(num - 1)



# 上面的代码中，fac函数中又调用了fac函数，这就是所谓的递归调用。
# 代码第6行的if条件叫做递归的收敛条件，简单的说就是什么时候要结束函数的递归调用，在计算阶乘时，如果计算到0或1的阶乘，就停止递归调用，直接返回1；
# 代码第8行的num * fac(num - 1)是递归公式，也就是阶乘的递归定义。


# 下面，我们简单的分析下，如果用fac(5)计算5的阶乘，整个过程会是怎样的。
# 递归调用函数入栈
# 5 * fac(4)
# 5 * (4 * fac(3))
# 5 * (4 * (3 * fac(2)))
# 5 * (4 * (3 * (2 * fac(1))))
# 停止递归函数出栈
# 5 * (4 * (3 * (2 * 1)))
# 5 * (4 * (3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120
print(fac(5))    # 120



#注意，函数调用会通过内存中称为“栈”（stack）的数据结构来保存当前代码的执行现场，函数调用结束后会通过这个栈结构恢复之前的执行现场。
# 栈是一种先进后出的数据结构，这也就意味着最早入栈的函数最后才会返回，而最后入栈的函数会最先返回。
# 例如调用一个名为a的函数，函数a的执行体中又调用了函数b，函数b的执行体中又调用了函数c，那么最先入栈的函数是a，最先出栈的函数是c。
# 每进入一个函数调用，栈就会增加一层栈帧（stack frame），栈帧就是我们刚才提到的保存当前代码执行现场的结构；
# 每当函数调用结束后，栈就会减少一层栈帧。通常，内存中的栈空间很小，因此递归调用的次数如果太多，会导致栈溢出（stack overflow），
# 所以递归调用一定要确保能够快速收敛。
# 我们可以尝试执行fac(5000)，看看是不是会提示RecursionError错误，错误消息为：maximum recursion depth exceeded in comparison（超出最大递归深度），其实就是发生了栈溢出。

#我们使用的Python官方解释器，默认将函数调用的栈结构最大深度设置为1000层。
# 如果超出这个深度，就会发生上面说的RecursionError。
# 当然，我们可以使用sys模块的setrecursionlimit函数来改变递归调用的最大深度，
# 例如：sys.setrecursionlimit(10000)，这样就可以让上面的fac(5000)顺利执行出结果，
# 但是我们不建议这样做，因为让递归快速收敛才是我们应该做的事情，否则就应该考虑使用循环递推而不是递归。




