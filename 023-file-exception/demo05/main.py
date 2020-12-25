#异常处理机制

# 为了让代码具有健壮性和容错性，我们可以使用Python的异常机制对可能在运行时发生状况的代码进行适当的处理。
# Python中和异常相关的关键字有五个，分别是try、except、else、finally和raise，我们先看看下面的代码，再来为大家介绍这些关键字的用法。


file = None
try:
    file = open('致橡树.txt', 'r', encoding='utf-8')
    print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
finally:
    if file:
        file.close()



# 在Python中，我们可以将运行时会出现状况的代码放在try代码块中，在try后面可以跟上一个或多个except块来捕获异常并进行相应的处理。
# 例如，在上面的代码中，文件找不到会引发FileNotFoundError，
# 指定了未知的编码会引发LookupError，
# 而如果读取文件时无法按指定编码方式解码文件会引发UnicodeDecodeError，
# 所以我们在try后面跟上了三个except分别处理这三种不同的异常状况。
# 在except后面，我们还可以加上else代码块，这是try 中的代码没有出现异常时会执行的代码，而且else中的代码不会再进行异常捕获，也就是说如果遇到异常状况，程序会因异常而终止并报告异常信息。
# 最后我们使用finally代码块来关闭打开的文件，释放掉程序中获取的外部资源。
# 由于finally块的代码不论程序正常还是异常都会执行，甚至是调用了sys模块的exit函数终止Python程序，finally块中的代码仍然会被执行（因为exit函数的本质是引发了SystemExit异常），
# 因此我们把finally代码块称为“总是执行代码块”，它最适合用来做释放外部资源的操作。