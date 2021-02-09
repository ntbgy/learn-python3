#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：06.01.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021-01-26 21:54
"""
英文字符频率统计。编写一个程序，对给定字符串中出现的 a~z 字母频率进行分析，忽略大小写，采用降序方式输出。
"""
s = """
lsadkgjadskglkhldkjfhkjKJHIUOUYOJHLljad1415445!#$!#@$fkh 
fajdhfloiuykjdanfkjahdf;hdhkajdshflhadjfhejehfiuewqhjkahdfkjadsh
"""
s = s.lower()
zhi_mu = dict()
for x in s:
    if x >= 'a' and x <= 'z':
        zhi_mu[x] = zhi_mu.get(x, 0) + 1
zhi_mu = list(zhi_mu.items())
zhi_mu.sort(key=lambda x: x[1], reverse=True)
for i in range(len(zhi_mu)):
    x, count = zhi_mu[i]
    print("{0:<3} {1:>5}".format(x, count))
