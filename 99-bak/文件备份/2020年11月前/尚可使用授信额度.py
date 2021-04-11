import random
from sys import path
import xlrd  # 读取excel文件
from xlrd import sheet
from xlrd.formula import rownamerel
import xlwt
import time

# excel_name = '个人违约贷款担保情况统计表__'
excel_name = '授信情况表__'
excel_path = 'D:\Work\贵阳农商监管报送平台\新版客户风险\%s.xlsx' % (excel_name)

# 打开文件(默认以rb方式打开)
f = xlrd.open_workbook(excel_path)

# 根据sheet索引或者名称获取sheet内容
sheet_f = f.sheet_by_index(0)
row_1 = sheet_f.row_values(1)
print(excel_name + ".xlsx")

sheet_name = time.strftime('%Y%m%d')
checktime = time.strftime('%Y_%m_%d_%H_%M_%S')
f_1 = xlwt.Workbook(encoding='utf-8')  # 设置字符类型， 默认 ascii 类型
sheet_1 = f_1.add_sheet(sheet_name, cell_overwrite_ok=True)
style0 = xlwt.easyxf('font: name 黑体, bold on')
style1 = xlwt.easyxf('font: name 宋体, ')

for i in range(0, len(row_1)):
    sheet_1.write(0, i, row_1[i], style0)

temp = 0
for i in range(2, sheet_f.nrows - 1):
    row_n = sheet_f.row_values(i)
    # H.授信额度 row_n[12] I.其中：贷款授信额度 row_n[13]
    # Q.现有业务余额占用授信额度 row_n[19] R.其中：贷款余额占用贷款授信额度 row_n[20]
    # T.其中：尚可使用贷款授信额度 row_n[21] T.其中：尚可使用贷款授信额度 row_n[22]
    # row_n[12] - row_n[19] = row_n[21]
    # row_n[13] - row_n[20] = row_n[22]
    # row_n[12].replace(" ", "")
    # row_n[19].replace(" ", "")
    # row_n[21].replace(" ", "")
    # print('12', row_n[12], isinstance(row_n[12], float))
    # print('19', row_n[19], isinstance(row_n[19], float))
    # print('20', row_n[20], isinstance(row_n[20], float))
    if isinstance(row_n[12], str) == False and \
            isinstance(row_n[19], str) == False and \
            isinstance(row_n[21], str) == False and \
            isinstance(row_n[13], str) == False and \
            isinstance(row_n[20], str) == False and \
            isinstance(row_n[22], str) == False and \
            (float(row_n[12]) - float(row_n[19]) != float(row_n[21]) \
             or float(row_n[13]) - float(row_n[20]) != float(row_n[22])):
        temp += 1
        for x in range(len(row_n)):
            sheet_1.write(temp, x, row_n[x], style1)

print(temp)
f_1.save(r"D:\Work\贵阳农商监管报送平台\新版客户风险\核对结果\%s_核对不上_%s.xls" % (excel_name, checktime))
