#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：03.02.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-30 9:35
"""
获得用户输入的一个字符串，将字符串按照空格分隔，然后逐行打印出来。
"""
s = input('请输入一个字符串：')
l = s.split(' ')
for x in l:
    print(x)
