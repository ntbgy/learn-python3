#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：07.01.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021/2/9 11:01
"""
输入一个文件和一个字符，统计该字符在文件中出现的次数。
"""


def 统计字符次数(文件名称, 字符):
    with open(文件名称, 'r', encoding='utf-8') as fr:
        计数 = 0
        for x in fr.read():
            if x == 字符:
                计数 += 1
    return 计数


if __name__ == '__main__':
    文件名称 = '07.01.txt'
    字符 = input('请输入一个字符：')
    print("字符 {} 在 {} 中出现次数为 {} 次".format(字符, 文件名称, 统计字符次数(文件名称, 字符)))
