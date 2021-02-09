#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：05.03.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021-01-12 13:20
"""
编写一个函数计算传入字符串中数字、字母、空格以及其它字符的个数。
"""


def fun(s):
    shu_zhi, zhi_mu, kong_ge, qi_ta = 0, 0, 0, 0
    for x in s:
        if x in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            shu_zhi += 1
        elif x.upper() >= 'A' and x.upper() <= 'Z':
            zhi_mu += 1
        elif x == ' ':
            kong_ge += 1
        else:
            qi_ta += 1
    return shu_zhi, zhi_mu, kong_ge, qi_ta


if __name__ == '__main__':
    s = input('请输入一行字符串：')
    l = fun(s)
    print("数字：{}，字母：{}，空格：{}，其它：{}".format(l[0], l[1], l[2], l[3]))
