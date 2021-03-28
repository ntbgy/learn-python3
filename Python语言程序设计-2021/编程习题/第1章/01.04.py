#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：01.04.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-28 12:42
"""
系统循环提示输入用户三个爱好并一起输出。
"""
hobbies = ""
for i in range(3):
    s = input('请输入你的爱好（最多三个，按Q或q结束）：')
    if s.upper() == 'Q':
        break
    hobbies += s + ' '
print("你的爱好是：", hobbies)
