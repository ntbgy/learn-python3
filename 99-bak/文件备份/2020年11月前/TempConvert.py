# TempConvert.py
# /usr/bin/python3
# -*- coding: utf-8 -*-
TempStr = input("请输入带有符号的温度值(9Fa 8fa 8ce 9Ce)：")
if TempStr[-2:] in ['Fa', 'fa']:
    C = (eval(TempStr[0:-2]) - 32) / 1.8
    print("转换后的温度是{:.2f}Ce".format(C))
elif TempStr[-2:] in ['Ce', 'ce']:
    F = 1.8 * eval(TempStr[0:-2]) + 32
    print("转换后的温度是{:.2f}Fa".format(F))
else:
    print("输入格式错误")
