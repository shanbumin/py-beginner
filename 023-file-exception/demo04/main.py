# 如果要向文件中写入内容，可以在打开文件时使用w或者a作为操作模式，前者会截断之前的文本内容写入新的内容，
# 后者是在原来内容的尾部追加新的内容。


file = open('../oak.txt', 'a', encoding='utf-8')
file.write('\n标题：《致橡树》')
file.write('\n作者：舒婷')
file.write('\n时间：1977年3月')
file.close()


# 也可以使用下面的代码来完成相同的操作。


lines = ['标题：《致橡树》', '作者：舒婷', '时间：1977年3月']
file = open('../oak.txt', 'a', encoding='utf-8')
for line in lines:
    file.write(f'\n{line}')
file.close()