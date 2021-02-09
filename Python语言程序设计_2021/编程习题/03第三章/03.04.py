#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：03.04.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-30 10:47
"""
设n是一个任意自然数，如果n的各位数字反向排列所得自然数与n相等，则n被称为回文数。从键盘输入一个5位数字，请编写程序判断这个数字是不是回文数。
"""
n = str(eval(input('请输入一个五位数字：')))
if len(n) == 5:
    if n == n[::-1]:
        print("是")
    else:
        print("否")
else:
    print("输入错误")
