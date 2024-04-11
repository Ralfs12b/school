import turtle
import random



garums = random.randint(10, 200)
krāsa = ["red", "blue", "green", "black", "pink", "brown"]
lenķis = random.randint(1, 90)
lenght = garums
color = krāsa

turtle.speed(10)

def rantur():
      turtle.fillcolor(random.choice(color))
      turtle.begin_fill()
      turtle.pencolor(random.choice(color))
      for i in range(4):
            turtle.forward(lenght)
            turtle.right(90)

def randomm():
      for i in range(5):
            rantur()
            turtle.penup()
            turtle.goto(random.randint(-250,0), random.randint(0,250))
            turtle.pendown()
            
randomm()

turtle.done()
