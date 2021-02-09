#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：02.05.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-29 20:37
"""
获得用户输入的一个整数N，计算并输入1到N相加的和。
"""
n = eval(input('请输入整数N：'))
sum = 0
for i in range(1, n + 1):
    sum += i
print(sum)
