#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：06.05
# 开发工具：PyCharm
# 开发人员：Admin
# 开发时间：2021/2/1 20:05
"""
重复元素续。利用集合的无重复性改编上一个程序，获得一个更快更简介的版本。
"""


def cfyspd(li):
    s = set()
    for i in range(len(li)):
        s.add(li[i])
    if len(s) == len(li):
        return True
    else:
        return False


if __name__ == '__main__':
    print(cfyspd([1, 2, 3, 3]))
    print(cfyspd([1, 2, 3, 4]))
