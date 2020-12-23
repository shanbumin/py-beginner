

items = ['Python', 'Java', 'Go', 'Swift']
# 对列表进行遍历的时候，使用了enumerate函数，这个函数非常有用。我们之前讲过循环遍历列表的两种方法，一种是通过索引循环遍历，一种是直接遍历列表元素。
# 通过enumerate处理后的列表在循环遍历时会取到一个二元组，解包之后第一个值是索引，第二个值是元素，下面是一个简单的对比。
for index in range(len(items)):
    print(f'{index}: {items[index]}')

print("_"*100)
for index, item in enumerate(items):
    print(f'{index}: {item}')




