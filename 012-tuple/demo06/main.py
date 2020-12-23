"""
例子3：让函数返回多个值。
"""



def  find_max_and_min(items):
    """
    找出列表中最大和最小的元素
    :param items: 列表
    :return: 最大和最小元素构成的二元组
    :author  sam@2020-12-23 13:55:50
    """
    max_one, min_one = items[0], items[0]
    for item in items:
        if item > max_one:
            max_one = item
        elif item < min_one:
            min_one = item
    return max_one, min_one



print(find_max_and_min([1,2,3,10,0]))
