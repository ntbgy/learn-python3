#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：05.01.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021-01-12 11:58
"""
实现isNull()函数，参数为一个字符串，如果这个字符串属于整数、浮点数或复数的表示，则返回True，否则返回False。
"""


def isNull(s):
    try:
        s = eval(s)
        if isinstance(s, int) or isinstance(s, float) or isinstance(s, complex):
            return True
        else:
            return False
    except NameError:
        return False


if __name__ == '__main__':
    s = input('请输入一行字符串：')
    print(isNull(s))
