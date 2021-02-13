#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：07.04.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021/2/10 16:13
"""
编写一个程序，读取一个 Python 源代码文件，将文件中所有除保留字以外的小写字母换成大写字母，生成的文件要能够被 Python 解释器正确执行。
"""
import keyword
保留字列表 = keyword.kwlist
def python代码字母大写(源代码, 新代码):
    with open(源代码, 'r', encoding='utf-8') as fr:
        for 行 in fr.readlines():
            行 = 行.split()
            for 词 in 行:
                if 词 in 保留字列表:
                    pass
                else:
                    词.upper()
                print(词)
if __name__ == '__main__':
    python代码字母大写('07.01.py', 'new.07.01.py')