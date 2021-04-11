#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# BMI.py


def print_bmi_zgbz():
    print("---------------------------")
    # BMI中国标准
    print("欢迎来到BMI Python 计算器")
    print("BMI中国标准")
    print("偏瘦  <=  18.4")
    print("正常  18.5--23.9")
    print("过重  24.0--27.9")
    print("肥胖  >=  28.0")
    print("---------------------------")


print_bmi_zgbz()
height = float(input("请输入你的身高（cm）："))
weight = float(input("请输入你的体重（kg）："))


def BMI(height, weight):
    height = height / 100
    BMI = weight / (height ** 2)
    return BMI


b = BMI(height, weight)
if b <= 18.4:
    print('身体状态:偏瘦')
elif b <= 23.9:
    print('身体状态:正常')
elif b <= 27.9:
    print('身体状态:超重')
elif b >= 28:
    print('身体状态:肥胖')
print("BMI = %.2f " % b)
