# SevenDigitsDrawV2.py
import turtle, time


def drawGap():  # 绘制数码管间隔
    turtle.penup()
    turtle.fd(5)


def drawLine(draw):  # 绘制单段数码管
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    turtle.fd(40)
    drawGap()
    turtle.right(90)


def drawDigit(d):  # 根据数字绘制七段数码管
    drawLine(True) if d in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if d in [0, 4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if d in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()
    turtle.fd(20)


def drawDot():
    turtle.pendown()
    turtle.fd(1)
    turtle.penup()


def drawDate(date):
    turtle.pencolor("red")
    # print(date)
    for i in date:
        if i == '-':
            drawDot()
            turtle.pencolor("green")
            turtle.fd(20)
        elif i == '=':
            drawDot()
            turtle.pencolor("blue")
            turtle.fd(30)
        elif i == '+':
            turtle.write('', font=("Arial", 18, "normal"))
        else:
            drawDigit(eval(i))


def main():
    turtle.setup(800, 350, 200, 200)
    while True:
        turtle.tracer(False)  # 不显示绘制过程，直接显示结果
        turtle.reset()
        turtle.penup()
        turtle.fd(-350)
        turtle.pensize(5)
        drawDate(time.strftime('%H-%M=%S+'))
        turtle.hideturtle()
        time.sleep(1)
    turtle.done()


main()
