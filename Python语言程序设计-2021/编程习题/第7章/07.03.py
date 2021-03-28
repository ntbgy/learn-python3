#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：07.03.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2021/2/10 16:02
"""
编写一个程序，生成一个 10×10 的随机矩阵并保存为文件（空格分隔行向量、换行分割列向量），
再写程序将刚才保存的矩阵文件另存为 CSV 格式，
用 Excel 或文本编辑器打开看看结果对不对。
"""
import random


def s_txt(low, high, txtname):
    f = open("{}.txt".format(txtname), "w")
    for line in range(10):
        word = ""
        for row in range(10):
            word = word + str(random.randrange(low, high)) + " "
        f.write(word + "\n")
    f.close()


def s_csv(txtname, csvname):
    f1 = open("{}.txt".format(txtname), "r")
    f2 = open("{}.csv".format(csvname), "w")
    for line in f1:
        after = line.replace(" ", ",")
        f2.write(after)
    f1.close()
    f2.close()


def main():
    low, high = eval(input("请输入随机数下限low、上限high，并用逗号隔开："))
    txtname = input("请输入txt文件名：")
    s_txt(low, high, txtname)
    csvname = input("请输入csv文件名：")
    s_csv(txtname, csvname)


main()
