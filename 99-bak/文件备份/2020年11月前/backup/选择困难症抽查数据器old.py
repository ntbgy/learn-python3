import random
from sys import path
import xlrd  # 读取excel文件法定代表人、高管及重要关联人信息表__
from xlrd import sheet

# excel_name = '个人违约贷款担保情况统计表__'
# excel_name = '授信情况表__'
# excel_name = '贷款明细表__' 表外业务明细表__
# excel_name = '表外业务明细表__'
excel_name = input("Excel名字，不要后缀名：\n")
excel_path = 'D:\Work\贵阳农商监管报送平台\新版客户风险\%s.xlsx' % (excel_name)

# 打开文件(默认以rb方式打开)
f = xlrd.open_workbook(excel_path)

# 根据sheet索引或者名称获取sheet内容
sheet_f = f.sheet_by_index(0)
row_1 = sheet_f.row_values(1)

print('=.=' * 20)
print('\t \t 选择困难症抽查数据器')
print('-.-' * 20)
print("\t \t " + excel_name)
print('-.-' * 20)

row0 = ['行', row_1[0], row_1[1], ]
print('行 \t %s \t \t  %s' % (row_1[0], row_1[1]))

for i in range(0, 5):
    t = random.randint(2, sheet_f.nrows - 1)
    row_n = sheet_f.row_values(t)
    print('%s \t %s \t %s' % (t + 1, row_n[0], row_n[1]))

print('=.=' * 20)

# print(excel_name +"\n"+ excel_path)
