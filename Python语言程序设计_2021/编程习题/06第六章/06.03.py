#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：06.03
# 开发工具：PyCharm
# 开发人员：Admin
# 开发时间：2021/2/1 19:28
"""
随机密码生成。编写一个程序，在26个字母大小写和9个数字组成的列表中随机生成 10 个 8 位密码。
"""
import random

s = (
"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
"Y", "Z",
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
"y", "z",
"0", "1", "2", "3", "4", "5", "6", "7", "8", "9",)

# s2 = list()
# for i in range(26):
#     if i < 10:
#         s2.append(i)
#     s2.append(chr(ord('A') + i))
#     s2.append(chr(ord('a') + i))
# print(s2)


# for i in range(26):
#     print('"{}", '.format(chr(ord('A') + i)), end='')
# for i in range(26):
#     print('"{}", '.format(chr(ord('a')+i)), end='')
# for i in range(10):
# print('"{}", '.format(i), end='')
# 方法1：
for i in range(10):  # 循环10遍，生成10组密码
    for i in range(8):
        print(random.choice(s), end="")  # random.choice(seq)实现从序列或集合seq中随机选取一个元素
    print()  # 每输出一组后，换行输出下一组

# 方法2：
for i in range(10):  # 循环10遍，生成10组密码
    k = random.sample(s, 8)  # random.sample(seq, k)实现从序列或集合seq中随机选取k个独立的的元素,以列表形式输出
    for i in k:  # 遍历随机数组中的每一项并输出
        print(i, end="")
    print()  # 每输出一组后，换行输出下一组
