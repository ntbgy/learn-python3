#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 文件名称：绘制五星红旗.py
# 开发工具：PyCharm
# 开发人员：ntbgy
# 开发时间：2020-12-26 16:16
import turtle as t

# 不展示绘制过程
t.tracer(False)


# 大星星
def dxx():
    t.color('yellow', 'yellow')
    t.begin_fill()
    for i in range(5):
        t.fd(90)
        t.right(144)
    t.end_fill()


# 小星星
def xxx():
    t.color('yellow', 'yellow')
    t.begin_fill()
    for i in range(5):
        t.fd(25)
        t.right(144)
    t.end_fill()


# 红布
t.setup(600, 400)
t.color('red', 'red')
t.begin_fill()
t.up()
t.goto(-250, 150)
t.pd()
t.goto(250, 150)
t.goto(250, -150)
t.goto(-250, -150)
t.goto(-250, 150)
t.end_fill()
# 大星星位置
t.up()
t.goto(-200, 85)
t.pd()
dxx()
# 小星星1位置
t.left(45)
t.up()
t.goto(-98, 120)
t.pd()
xxx()
# 小星星2位置
t.left(45)
t.up()
t.goto(-70, 70)
t.pd()
xxx()
# 小星星3位置
t.left(45)
t.up()
t.goto(-60, 28)
t.pd()
xxx()
# 小星星4位置
t.left(45)
t.up()
t.goto(-88, 0)
t.pd()
xxx()
# 隐藏小海龟
t.hideturtle()
# 大功告成!!!
t.done()
