#将数据写入CSV文件
# 要达成这个目标，可以使用Python标准库中的csv模块，该模块的writer函数会返回一个csvwriter对象，
# 通过该对象的writerow或writerows方法就可以将数据写入到CSV文件中，具体的代码如下所示。
'''
姓名,语文,数学,英语
关羽,57,52,94
张飞,76,93,60
赵云,78,67,39
马超,60,64,91
黄忠,83,54,84
'''

import csv
import random

with open('../demo02/scores.csv', 'w') as file:
    writer = csv.writer(file)
    #先写入1行
    writer.writerow(['姓名', '语文', '数学', '英语'])
    #准备写入5行
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    for i in range(5): #遍历5行
        verbal = random.randint(50, 100) #语文
        math = random.randint(40, 100)  #数学
        english = random.randint(30, 100)  #英语
        writer.writerow([names[i], verbal, math, english])


# 需要说明的是上面的writer函数，该函数除了传入要写入数据的文件对象外，还可以dialect参数，它表示CSV文件的方言，默认值是excel。
# 除此之外，还可以通过delimiter、quotechar、quoting参数来指定分隔符（默认是逗号）、包围值的字符（默认是双引号）以及包围的方式。
# 其中，包围值的字符主要用于当字段中有特殊符号时，通过添加包围值的字符可以避免二义性。
# 大家可以尝试将上面第5行代码修改为下面的代码，看看生成的CSV文件到底有什么区别。
# writer = csv.writer(file, delimiter='|', quoting=csv.QUOTE_ALL)