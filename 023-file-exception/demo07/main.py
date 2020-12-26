# 对于open函数返回的文件对象，还可以使用with上下文语法在文件操作完成后自动执行文件对象的close方法，这样可以让代码变得更加简单，
# 因为不需要再写finally代码块来执行关闭文件释放资源的操作。
# 需要提醒大家的是，并不是所有的对象都可以放在with上下文语法中，只有符合上下文管理器协议（有__enter__和__exit__魔术方法）的对象才能使用这种语法，
# Python标准库中的contextlib模块也提供了对with上下文语法的支持，后面再为大家进行讲解。

try:
    with open('../oak.txt', 'r', encoding='utf-8') as file:
        print(file.read())
except FileNotFoundError:
    print('无法打开指定的文件!')
except LookupError:
    print('指定了未知的编码!')
except UnicodeDecodeError:
    print('读取文件时解码错误!')
