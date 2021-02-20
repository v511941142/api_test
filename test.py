import xlrd
from xlutils.copy import copy

value = ['xiaoming','man',22,',china']    #定义需要写入的文本

rb = xlrd.open_workbook(r'D:\data.xls')   #打开一个工作薄
wb = copy(rb)                             #复制工作簿

writeSheet = wb.get_sheet(2)              #通过get_sheet方法找到sheet页

writeSheet.write(1,2,value[0])            #写入单元格，1,2分别指的是单元格坐标，value[0]是具体写入的值

wb.save(r'D:\data.xls')                   #最后保存工作薄
print('ok')