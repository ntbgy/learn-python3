#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：03.05.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-30 11:32
"""
输入一个十进制整数，分别输出其二进制、八进制、十六进制字符串。
"""
n = int(eval(input('请输入一个十进制整数：')))
print("二进制：{}".format(bin(n)))
print("八进制：{}".format(oct(n)))
print("十六进制：{}".format(hex(n)))
