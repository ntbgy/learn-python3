#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：04.02.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-30 15:28
"""
最大公约数计算。获得两个整数，求出这两个整数的最大公约数和最小公倍数。最大公约数计算一般用辗转相除法，最小公倍数计算则使用两个数的乘积，除以最大公约数。
"""
n1 = eval(input('请输入整数1：'))
n2 = eval(input('请输入整数2：'))

if min(n1, n2) == n1:
    n1, n2 = n2, n1


def zui_da_gong_yue_shu(n1, n2):
    while True:
        temp = n1 % n2
        if temp == 0:
            return n2
            break
        else:
            n1 = n2
            n2 = temp


def zui_xiao_gong_bei_shu(n1, n2):
    return int(n1 * n2 / zui_da_gong_yue_shu(n1, n2))


print("{}, {}\n最大公约数：{}，最大公倍数：{}".format(n1, n2, zui_da_gong_yue_shu(n1, n2), zui_xiao_gong_bei_shu(n1, n2)))
