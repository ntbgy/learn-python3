#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：04.03.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-30 16:07
"""
统计不同字符个数。用户从键盘输入一行字符，编写一个程序，统计并输出其中英文字符、数字、空格和其它字符的个数。
"""
s = input('请输入一行字符串：')
en, nu, sp, ot = 0, 0, 0, 0
for x in s:
    if x.upper() >= 'A' and x.upper() <= 'Z':
        en += 1
    elif x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        nu += 1
    elif x == ' ':
        sp += 1
    else:
        ot += 1
print("{}\n英文字符：{}\n数字：{}\n空格：{}\n其它字符：{}".format(s, en, nu, sp, ot))
