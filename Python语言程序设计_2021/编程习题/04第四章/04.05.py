#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：04.05.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021-01-09 14:28
"""
羊车门问题。有三扇关闭的门，一扇门后面停着汽车，其余门后是山羊，只有主持人知道每扇门后面是什么。参赛者可以选择一扇门，在开启它之前，主持人会开启另一扇门，露出门后的山羊，然后允许参赛者更换自己的选择。请问参赛者更换选择后能否增加猜中汽车的机会？——这是一个经典的问题。请使用 random 库对这个随机事件进行预测，分别输出参赛者改变选择和坚持选择获胜的概率。
"""
import random

T = 10000
count, gai_bian, jian_chi = 0, 0, 0
while True:
    xuan_zhe = random.randint(1, 3)
    shi_ji = random.randint(1, 3)
    if xuan_zhe == shi_ji:
        jian_chi += 1
    else:
        gai_bian += 1
    count += 1
    if count == T:
        break
print("参赛者改变选择获胜的概率：{:.2f}\n参赛者坚持选择获胜的概率：{:.2f}".format(gai_bian / T, jian_chi / T, ))
