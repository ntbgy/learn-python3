#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：05.02.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021-01-12 12:24
"""
实现isPrime()函数，参数为整数，要有异常处理。如果整数是质数，返回True，否则返回False。
"""


def isPrime(n):
    try:
        if isinstance(n, int):
            pass
        else:
            n = eval(n)
        if isinstance(n, int):
            if n <= 1:
                return False
            elif n in [2, 3]:
                return True
            else:
                for i in range(2, int(pow(n, 0.5)) + 1):
                    if n % i == 0:
                        return False
                return True
        else:
            return False
    except:
        return False


if __name__ == '__main__':
    n = input('请输入一个整数：')
    print(isPrime(n))
