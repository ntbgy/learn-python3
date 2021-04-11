#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：递归打印当前目录下所有文件（自定义查找文件类型）.py.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-26 16:06
import os


def search(str, path='../'):
    for x in os.listdir(path):
        if os.path.isdir(x):
            new_path = os.path.join(path, x)
            search(str, new_path)
        else:
            if str in x:
                print(os.path.join(path, x))


if __name__ == '__main__':
    search('.txt')
