# PythonDraw.py
# /usr/bin/python3
import turtle

# turtle.setup(width, height, startx, starty)
turtle.setup(650, 350, 200, 200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
# 蟒蛇颜色
turtle.pencolor("purple")
turtle.seth(-40)
# 蟒蛇节数
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)
# 蟒蛇头方向
turtle.circle(16, 120)
# 蟒蛇头长度
turtle.fd(40 * 2 / 3)
turtle.done()
