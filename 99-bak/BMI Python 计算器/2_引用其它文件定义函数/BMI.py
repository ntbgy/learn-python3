#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# BMI.py
import time
# 身体质量指数 (Body Mass Index, 简称BMI), 亦称克托莱指数, 是目前国际上常用的衡量人体胖瘦程度以及是否健康的一个标准。
# BMI 值超标，意味着你必须减肥了。
# 体质指数（BMI）=体重（kg）÷身高（m）的平方
# 调用BMI标准打印函数
from print_bmi_zgbz import print_bmi_zgbz

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
print("程序将在10秒后结束！")
time.sleep(10)
