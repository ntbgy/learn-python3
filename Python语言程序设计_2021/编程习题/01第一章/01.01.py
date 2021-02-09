#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：01.01.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-28 12:23
"""
根据用户输入的内容输出相应的结果。
"""
name = input('请输入对方名字：')
s = input('请输入悄悄话内容：')
print("{},听我说句悄悄话：{}".format(name, s * 3))
