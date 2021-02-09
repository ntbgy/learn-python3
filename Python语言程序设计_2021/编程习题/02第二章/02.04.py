#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：02.04.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-29 20:29
"""
获得用户输入的一个小数，提取并输出其整数部分。
"""
n = input('请输入一个小数：')
for x in n:
    if x == '.':
        break
    print(x, end='')
