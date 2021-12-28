import turtle
import random
tao = turtle.Turtle()
color1 = ["red","blue","green"]
for i in range(1,11):
    x = random.randint(-500,500)
    y = random.randint(-500,500)
    c = random.choice(color1)
    f = random.randint(50,100)
    tao.penup()
    tao.goto(x,y)
    tao.color(c)
    tao.pendown()
    for j in range(1,5):
        tao.forward(f)
        tao.left(90)
    tao.penup
