#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：01.05.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-28 14:09
"""
系统提示输入用户名字，并随机生成一个幸运数字，输出结果。
"""
import random

str1 = input('请输入你的名字：')
print("Hello! {}".format(str1))
guard = ord(str1[0]) % 100
print("你的幸运数字是", random.choice(range(guard)))
