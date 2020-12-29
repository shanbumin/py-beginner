#读excel

import xlrd

# 使用xlrd模块的open_workbook函数打开指定Excel文件并获得Book对象（工作簿）
wb = xlrd.open_workbook('考试成绩表.xlsx')
# 通过Book对象的sheet_names方法可以获取所有表单名称
sheetname = wb.sheet_names()[0]
# 通过指定的表单名称获取Sheet对象（工作表）
sheet = wb.sheet_by_name(sheetname)
# 通过Sheet对象的nrows和ncols属性获取表单的行数和列数
print(sheet.nrows, sheet.ncols)





for row in range(sheet.nrows): #一行行遍历
    for col in range(sheet.ncols): #一列列遍历
        # 通过Sheet对象的cell方法获取指定Cell对象（单元格）
        # 通过Cell对象的value属性获取单元格中的值
        value = sheet.cell(row, col).value
        # 对除首行外的其他行进行数据格式化处理
        if row > 0:
          print(value, end='\t')
    print()



# 获取最后一个单元格的数据类型
# 0 - 空值，1 - 字符串，2 - 数字，3 - 日期，4 - 布尔，5 - 错误
last_cell_type = sheet.cell_type(sheet.nrows - 1, sheet.ncols - 1)
print(last_cell_type)



# 获取第一行的值（列表）
print(sheet.row_values(0))


