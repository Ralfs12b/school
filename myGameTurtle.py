
import turtle

stage = turtle.Screen()
stage.bgcolor("black")
stage.title("Wecome to my game")

b = turtle.Turtle()
b.color("red")
b.penup()
b.setpos(-250, -250)
b.pendown()
b.pensize(3)
for i in range(4):
    b.forward(500)
    b.right(90)
b.hideturtle()

f = turtle.Turtle()
f.color("white")
f.shape("turtle")

positions = []

def up():
    f.setheading(90)

def down():
    f.setheading(180)

def left():
    f.setheading(270)

def right():
    f.setheading(0)

stage.listen()
stage.onkey(up, "Up")
stage.onkey(down, "Down")
stage.onkey(left, "Left")
stage.onkey(right, "Right")

While True:
    f.forward(0.05)
    if f.xcor() > 240 or f.xcor() < -240:
        break:
    if f.ycor() > 240 or f.ycor() < -240:
    break:

    position = (f.xcor(), f.ycor())

    if position in positions:
        break:
    else:
        positions.append(position)



