# 字符串的方法
#在Python中，我们可以通过字符串类型自带的方法对字符串进行操作和处理，对于一个字符串类型的变量，我们可以用变量名.方法名()的方式来调用它的方法。
# 所谓方法其实就是跟某个类型的变量绑定的函数，后面我们讲面向对象编程的时候还会对这一概念详加说明。


#-------------------------------------大小写相关操作-------------------------------------------------------

s1 = 'hello, world!'

# 使用capitalize方法获得字符串首字母大写后的字符串
print(s1.capitalize())   # Hello, world!
# 使用title方法获得字符串每个单词首字母大写后的字符串
print(s1.title())        # Hello, World!
# 使用upper方法获得字符串大写后的字符串
print(s1.upper())        # HELLO, WORLD!

s2 = 'GOODBYE'
# 使用lower方法获得字符串小写后的字符串
print(s2.lower())        # goodbye

#-----------------------------------------查找操作-----------------------------------------

s = 'hello, world!'

# find方法从字符串中查找另一个字符串所在的位置
# 找到了返回字符串中另一个字符串首字符的索引
print(s.find('or'))        # 8
# 找不到返回-1
print(s.find('shit'))      # -1
# index方法与find方法类似
# 找到了返回字符串中另一个字符串首字符的索引
print(s.index('or'))       # 8
# 找不到引发异常
#print(s.index('shit'))     # ValueError: substring not found

#在使用find和index方法时还可以通过方法的参数来指定查找的范围，也就是查找不必从索引为0的位置开始。find和index方法还有逆向查找（从后向前查找）的版本，分别是rfind和rindex，代码如下所示。

s = 'hello good world!'

# 从前向后查找字符o出现的位置(相当于第一次出现)
print(s.find('o'))       # 4
# 从索引为5的位置开始查找字符o出现的位置
print(s.find('o', 5))    # 7
# 从后向前查找字符o出现的位置(相当于最后一次出现)
print(s.rfind('o'))      # 12

#-----------------------------------------性质判断-----------------------------------------
#可以通过字符串的startswith、endswith来判断字符串是否以某个字符串开头和结尾；还可以用is开头的方法判断字符串的特征，这些方法都返回布尔值，代码如下所示。

s1 = 'hello, world!'

# startwith方法检查字符串是否以指定的字符串开头返回布尔值
print(s1.startswith('He'))    # False
print(s1.startswith('hel'))   # True
# endswith方法检查字符串是否以指定的字符串结尾返回布尔值
print(s1.endswith('!'))       # True

s2 = 'abc123456'

# isdigit方法检查字符串是否由数字构成返回布尔值
print(s2.isdigit())    # False
# isalpha方法检查字符串是否以字母构成返回布尔值
print(s2.isalpha())    # False
# isalnum方法检查字符串是否以数字和字母构成返回布尔值
print(s2.isalnum())    # True

#-----------------------------------------格式化字符串---------------------------------------

#在Python中，字符串类型可以通过center、ljust、rjust方法做居中、左对齐和右对齐的处理。

s = 'hello, world'

# center方法以宽度20将字符串居中并在两侧填充*
print(s.center(20, '*'))  # ****hello, world****
# rjust方法以宽度20将字符串右对齐并在左侧填充空格
print(s.rjust(20))        #         hello, world
# ljust方法以宽度20将字符串左对齐并在右侧填充~
print(s.ljust(20, '~'))   # hello, world~~~~~~~~

#我们也可以用字符串的方法来完成字符串的格式
a = 321
b = 123
print('{0} * {1} = {2}'.format(a, b, a * b))


#-----------------------------------修剪操作----------------------------------


#字符串的strip方法可以帮我们获得将原字符串修剪掉左右两端空格之后的字符串。
# 这个方法非常有实用价值，通常用来将用户输入中因为不小心键入的头尾空格去掉，strip方法还有lstrip和rstrip两个版本，相信从名字大家已经猜出来这两个方法是做什么用的。

s = '   jackfrued@126.com  \t\r\n'
# strip方法获得字符串修剪左右两侧空格之后的字符串
print("|"+s.strip()+"|")    # jackfrued@126.com

