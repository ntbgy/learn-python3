#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：01.02.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-28 12:26
"""
九九乘法表输出。工整打印输出常用的九九乘法表。
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{} × {} = {:2}".format(j, i, i * j), end='\t')
    print()
