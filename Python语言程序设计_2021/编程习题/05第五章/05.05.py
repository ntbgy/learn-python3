#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：05.05.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021-01-13 19:28
"""
编写一个函数，参数为一个整数 n 。利用递归获取斐波拉契数列中的第 n 个数并返回。
"""


# 循环
def fun(n):
    if n in [1, 2]:
        return 1
    elif n > 2:
        x, y = 1, 1
        count = 2
        while True:
            x, y = x + y, x
            count += 1
            if count == n:
                return x
                break


# 递归
def Fibonacci(n):
    if n in [1, 2]:
        return 1
    elif n > 2:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


print(fun(4))
print(Fibonacci(4))
