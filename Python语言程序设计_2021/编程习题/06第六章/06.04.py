#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：06.04
# 开发工具：PyCharm
# 开发人员：Admin
# 开发时间：2021/2/1 19:56
"""
重复元素判定。编写一个函数，接受列表作为参数，如果一个元素在一个列表中出现了不只一次，则返回 True ，但不要改变原来列表的值。同时编写调用这个函数和输出测试结果的的程序。
"""


def cfyspd(li):
    for i in range(len(li)):
        for j in range(len(li)):
            if i == j:
                continue
            elif li[i] == li[j]:
                return False
    return True


if __name__ == '__main__':
    print(cfyspd([1, 2, 3, 3]))
    print(cfyspd([1, 2, 3, 4]))
