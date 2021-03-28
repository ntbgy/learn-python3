#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：07.02.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021/2/10 15:53
"""
假设有一个英文文本文件，编写一个程序读取其文件内容并将里面的大写字母变成小写字母，小写字母变成大写字母。
"""


def 字母大小写互换(源文件名, 新文件名):
    with open(源文件名, 'r', encoding='utf-8') as fr, open(新文件名, 'w', encoding='utf-8') as fw:
        for x in fr.read():
            if x >= 'a' and x <= 'z':
                x = x.upper()
            elif x >= 'A' and x <= 'Z':
                x = x.lower()
            fw.write(x)


if __name__ == '__main__':
    字母大小写互换('07.02.txt', '07.02.new.txt')
