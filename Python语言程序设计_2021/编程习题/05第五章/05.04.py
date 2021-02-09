#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：05.04.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021-01-12 13:44
"""
编写一个函数，打印200以内的所有素数，以空格分割。
"""


def fun():
    print('2 3', end=' ')
    for n in range(4, 200):
        for i in range(2, int(pow(n, 0.5)) + 1):
            if n % i == 0:
                break
            if int(pow(n, 0.5)) == i:
                print(n, end=' ')


if __name__ == '__main__':
    fun()
