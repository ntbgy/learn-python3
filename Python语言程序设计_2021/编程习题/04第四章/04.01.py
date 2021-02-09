#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：04.01.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-30 15:23
"""
输入一个年份，输出是否闰年。
闰年条件：能被4整除但不能被100整除，或者能被400整除的年份都是闰年。
"""
year = eval(input('请输入一个年份：'))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("{}年是闰年".format(year))
else:
    print("{}年不是闰年".format(year))
