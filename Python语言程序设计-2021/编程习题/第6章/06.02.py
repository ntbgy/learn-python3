#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：06.02.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021-01-26 22:06
"""
中文字符频率统计。编写一个程序，对给定字符串中出现的全部字符（含中文字符）频率进行分析，采用降序方式输出。
"""
s = """
11111111111111111111111111111111111111111
拉师傅的课件靠靠靠靠靠靠艰苦艰苦就看见lkadfsjghglkajhdglkjadhfgl;
kjahds;lgfkj&%^%(^%&(&*^*(^(*47365916494862309756240893  
  hljkfadsh中文字符频率统计。编写一个程序，对给定字符串中出
  现的全部字符（含中文字符）频率进行分析，采用降序方式输出。 
"""
s = s.lower()
s = s.replace(' ', '')
s = s.replace('\n', '')
zhi_fu = dict()
for x in s:
    zhi_fu[x] = zhi_fu.get(x, 0) + 1
zhi_fu = list(zhi_fu.items())
zhi_fu.sort(key=lambda x: x[1], reverse=True)
for i in range(len(zhi_fu)):
    x, count = zhi_fu[i]
    print("{0:<3} {1:>5}".format(x, count))
