#从CSV文件读取数据

# 如果要读取刚才创建的CSV文件，可以使用下面的代码，通过csv模块的reader函数可以创建出csvreader对象，该对象是一个迭代器，
# 可以通过next函数或for-in循环读取到文件中的数据。


import csv

with open('scores.csv', 'r') as file:
    reader = csv.reader(file, delimiter='|')
    for line in reader:
        print(reader.line_num, end='\t')
        for elem in line:
            print(elem, end='\t')
        print()

# 注意：上面的代码对csvreader对象做for循环时，每次会取出一个列表对象，该列表对象包含了一行中所有的字段。