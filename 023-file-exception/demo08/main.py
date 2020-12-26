# 读写二进制文件

#读写二进制文件跟读写文本文件的操作类似，
# 但是需要注意，在使用open函数打开文件时，
# 如果要进行读操作，操作模式是'rb'，如果要进行写操作，操作模式是'wb'。
# 还有一点，读写文本文件时，read方法的返回值以及write方法的参数是str对象（字符串），而读写二进制文件时，read方法的返回值以及write方法的参数是bytes-like对象（字节串）。
# 下面的代码实现了将当前路径下名为a.png的图片文件复制到b.png文件中的操作。

try:
    with open('a.png', 'rb') as file1:
        data = file1.read()
    with open('b.png', 'wb') as file2:
        file2.write(data)
except FileNotFoundError:
    print('指定的文件无法打开.')
except IOError:
    print('读写文件时出现错误.')
print('程序执行结束.')


