#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：03.01.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-30 9:21
"""
获得用户输入的一个整数，输出该整数百位及以上的数字。
"""
n = str(eval(input('请输入一个整数：')))
if len(n) < 3 and n[0] != '-':
    print(0)
elif len(n) >= 3 and n[0] != '-':
    print(n[0:-2])
elif len(n) < 4 and n[0] == '-':
    print(0)
else:
    print(n[1:-2])
