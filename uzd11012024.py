import turtle
import random

ok = turtle.Turtle()

ok.speed("fastest")

g = ["red", "blue", "green", "black", "pink", "brown"]
ok.color("black")

def penta(x, y):
      turtle.fillcolor(random.choice(g))
      turtle.begin_fill()
      turtle.pencolor(random.choice(g))
      ok.penup()
      ok.goto(x, y)
      ok.pendown()
      for i in range(17):
            ok.forward(100)
            ok.left(170)
            ok.forward(100)

turtle.onscreenclick(penta, 1)
turtle.listen()
turtle.done()

