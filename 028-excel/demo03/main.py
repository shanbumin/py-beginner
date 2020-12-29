
#调整单元格样式

# 在写Excel文件时，我们还可以为单元格设置样式，
# 主要包括字体（Font）、对齐方式（Alignment）、边框（Border）和背景（Background）的设置，xlwt对这几项设置都封装了对应的类来支持。
# 要设置单元格样式需要首先创建一个XFStyle对象，再通过该对象的属性对字体、对齐方式、边框等进行设定，
# 例如在上面的例子中，如果希望将表头单元格的背景色修改为黄色，可以按照如下的方式进行操作。



import random

import xlwt

student_names = ['关羽', '张飞', '赵云', '马超', '黄忠']
scores = [[random.randint(40, 100) for _ in range(3)] for _ in range(5)]




# 创建工作簿对象（Workbook）
wb = xlwt.Workbook()

# 创建工作表对象（Worksheet）
sheet = wb.add_sheet('一年级二班')



# 添加表头数据
#背景色
pattern = xlwt.Pattern()
pattern.pattern = xlwt.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = 5 # 0 - 黑色、1 - 白色、2 - 红色、3 - 绿色、4 - 蓝色、5 - 黄色、6 - 粉色、7 - 青色、
#字体
font = xlwt.Font()
font.name = '华文楷体'
font.height = 20 * 18
font.bold = True
font.italic = False
font.colour_index = 3
#垂直居中
align = xlwt.Alignment()
align.vert = xlwt.Alignment.VERT_CENTER
align.horz = xlwt.Alignment.HORZ_CENTER
#边框
borders = xlwt.Borders()
props = (('top', 'top_colour'), ('right', 'right_colour'), ('bottom', 'bottom_colour'), ('left', 'left_colour'))
for position, color in props:
    setattr(borders, position, xlwt.Borders.DASHED)
    setattr(borders, color, 5)


header_style = xlwt.XFStyle()
#header_style.pattern = pattern
header_style.font=font
header_style.alignment=align
header_style.borders = borders

titles = ('姓名', '语文', '数学', '英语')
for index, title in enumerate(titles):
    sheet.write(0, index, title,header_style) #0是第一行  index是列号


# 将学生姓名和考试成绩写入单元格
for row in range(len(scores)):
    #第row+1行,1列
    sheet.write(row + 1, 0, student_names[row])
    #按照(行,列)来写
    for col in range(len(scores[row])):
        sheet.write(row + 1, col + 1, scores[row][col])

# 保存Excel工作簿
wb.save('考试成绩表.xlsx')