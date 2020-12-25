# 除了使用文件对象的read方法读取文件之外，还可以使用for-in循环逐行读取或者用readlines方法将文件按行读取到一个列表容器中，代码如下所示。


import time

file = open('../oak.txt', 'r', encoding='utf-8')
for line in file:
    print(line, end='')
    time.sleep(0.5)
file.close()

print()
print("-"*100)

file = open('../oak.txt', 'r', encoding='utf-8')
lines = file.readlines()
for line in lines:
    print(line, end='')
    time.sleep(0.5)
file.close()
print()