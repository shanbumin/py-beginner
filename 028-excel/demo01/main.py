
#写入Excel文件

import random

import xlwt

student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
scores = [[random.randint(40, 100) for _ in range(3)] for _ in range(5)]




# 创建工作簿对象（Workbook）
wb = xlwt.Workbook()

# 创建工作表对象（Worksheet）
sheet = wb.add_sheet('一年级二班')



# 添加表头数据
titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    sheet.write(0, index, title) #0是第一行  index是列号


# 将学生姓名和考试成绩写入单元格
for row in range(len(scores)):
    #第row+1行,1列
    sheet.write(row + 1, 0, student_names[row])
    #按照(行,列)来写
    for col in range(len(scores[row])):
        sheet.write(row + 1, col + 1, scores[row][col])

# 保存Excel工作簿
wb.save('考试成绩表.xlsx')