import json


#在Python中，我们可以使用json模块将字典或列表以JSON格式写入到文件中，代码如下所示。
my_dict = {
    'name': '骆昊',
    'age': 40,
    'friends': ['王大锤', '白元芳'],
    'cars': [
        {'brand': 'BMW', 'max_speed': 240},
        {'brand': 'Audi', 'max_speed': 280},
        {'brand': 'Benz', 'max_speed': 280}
    ]
}
with open('../demo02/data.json', 'w') as file:
    json.dump(my_dict, file)
print('字典已经保存到data.json文件中')

# 执行上面的代码，会创建data.json文件，文件的内容如下所示，中文是用Unicode编码书写的。
# {"name": "\u9a86\u660a", "age": 40, "friends": ["\u738b\u5927\u9524", "\u767d\u5143\u82b3"], "cars": [{"brand": "BMW", "max_speed": 240}, {"brand": "Audi", "max_speed": 280}, {"brand": "Benz", "max_speed": 280}]}

