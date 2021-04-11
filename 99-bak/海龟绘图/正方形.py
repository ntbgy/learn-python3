import turtle

for i in range(8):
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    turtle.fd(80)
    turtle.penup()
    turtle.fd(10)
    turtle.right(45)

turtle.penup()
turtle.goto(0, -75)

for i in range(4):
    turtle.penup()
    turtle.fd(10)
    turtle.pendown()
    turtle.fd(80)
    turtle.penup()
    turtle.fd(10)
    turtle.right(90)

turtle.done()
