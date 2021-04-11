import random
from sys import path
import xlrd
from xlrd import sheet
import xlwt
import time

sheet_name = '抽查数据'
checktime = time.strftime('%Y_%m_%d_%H_%M_%S')

excel_name = input("请输入Excel名字，不要文件拓展名：\n")
excel_path = 'D:\Work\贵阳农商监管报送平台\新版客户风险\%s.xlsx' % (excel_name)

f = xlrd.open_workbook(excel_path)
f_w = xlwt.Workbook(encoding='utf-8')
sheet_w = f_w.add_sheet(sheet_name, cell_overwrite_ok=True)

style0 = xlwt.easyxf('font: name 黑体, bold on')
style1 = xlwt.easyxf('font: name 宋体, ')

sheet_f = f.sheet_by_index(0)
row_1 = sheet_f.row_values(1)

print('=.=' * 20)
print('\t \t 选择困难症抽查数据器')
print('-.-' * 20)
print("" + excel_name)
print('-.-' * 20)

row0 = ['行', row_1[0], row_1[1], ]
print('行 \t %s \t \t  %s' % (row_1[0], row_1[1]))

for x in range(len(row_1)):
    sheet_w.write(0, x, row_1[x], style0)
for i in range(5):
    t = random.randint(2, sheet_f.nrows - 1)
    row_n = sheet_f.row_values(t)
    print('%s \t %s \t %s' % (t + 1, row_n[0], row_n[1]))
    for x in range(len(row_n)):
        sheet_w.write((i + 1) * 2 - 1, x, row_n[x], style1)

f_w.save('D:\Work\贵阳农商监管报送平台\新版客户风险\%s_抽查数据.xls' % (excel_name))
print('=.=' * 20)
