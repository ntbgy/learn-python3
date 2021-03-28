#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：04.04.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021-01-09 14:09
"""
猜数字游戏续。当用户输入的不是整数（如字母、浮点数等）时，程序会终止执行退出。改编题目 1 中的程序，当用户输入错误时给出“输入内容必须为整数！”的提示，并让用户重新输入。
注：题目 1，在1 ~ 1000中不断地让用户循环输入猜测值，并根据猜测值和目标值之间的比较决定程序逻辑。
"""
import random

target = random.randint(1, 1000)
# print(target)
count = 1
while True:
    try:
        guess = eval(input('请输入一个整数：'))
        if isinstance(guess, int):
            if guess > target:
                print("猜大了。")
            elif guess < target:
                print("猜小了。")
            else:
                print("猜对了，共猜测{}次。".format(count))
                break
            count += 1
        else:
            print("输入内容必须为整数！")
            break
    except:
        print("输入内容必须为整数！")
        break
