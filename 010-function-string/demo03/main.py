from os.path import splitext
# 获取文件名的后缀名
def get_suffix(filename):
    pos = filename.rfind('.')   # 从字符串中逆向查找.出现的位置,如果pos为0,则表示类似.gitignore这种无后缀的，得舍弃
    return filename[pos + 1:] if pos > 0 else ''  # 通过切片操作从文件名中取出后缀名





print(get_suffix('readme.txt'))       # txt
print(get_suffix('readme.txt.md'))    # md
print(get_suffix('.readme'))          #
print(get_suffix('readme.'))          #
print(get_suffix('readme'))           #





# 上面的get_suffix函数还有一个更为便捷的实现方式，就是直接使用os.path模块的splitext函数，
# 这个函数会将文件名拆分成带路径的文件名和扩展名两个部分，然后返回一个二元组，
# 二元组中的第二个元素就是文件的后缀名（包含.），如果要去掉后缀名中的.，可以做一个字符串的切片操作，代码如下所示。


def get_suffix2(filename):
    return splitext(filename)[1][1:]




print(get_suffix2('readme.txt'))       # txt
print(get_suffix2('readme.txt.md'))    # md
print(get_suffix2('.readme'))          #
print(get_suffix2('readme.'))          #
print(get_suffix2('readme'))           #


