import turtle
import random

# turtle.speed(1000)

# uzdevums 1

# def taisn():
#     turtle.pencolor("black")
#     turtle.forward(200)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.right(90)
#     turtle.forward(200)
#     turtle.right(90)
#     turtle.forward(100)
#     turtle.penup()
#     turtle.goto(-50, -150) 
#     turtle.pendown()
#     turtle.forward(200)
#     turtle.right(90)
#     turtle.forward(300)
#     turtle.right(90)
#     turtle.forward(200)
#     turtle.right(90)
#     turtle.forward(300)
    

# taisn()


# uzdevums 2

ok = turtle.Turtle()

ok.speed("fastest")

g = ["red", "blue", "green", "black", "pink", "brown"]
ok.color("black")

def circle(x, y):
    ok.fillcolor(random.choice(g))
    ok.begin_fill()
    ok.pencolor(random.choice(g))
    ok.penup()
    ok.goto(x, y)
    ok.pendown()
    for i in range(1):
        ok.circle(10)
    ok.end_fill()

turtle.onscreenclick(circle, 1)
turtle.listen()

turtle.done()