import turtle

# turtle.fillcolor("Black")
# turtle.begin_fill()
# turtle.pencolor("Black")
# turtle.circle(100)
# turtle.end_fill()
# turtle.penup()
# turtle.forward(50, 20)
# turtle.pendown()
# turtle.circle(30)
# turtle.end_fill()
# turtle.penup()
# turtle.forward(-50, 20)
# turtle.pendown()
# turtle.circle(30)
# turtle.end_fill()

# turtle.done()

def penta():
      for i in range(5):
            turtle.pencolor("Red")
            turtle.forward(100)
            turtle.right(72)
      turtle.penup()
      turtle.forward(250)
      turtle.pendown()

def cikls():
      for i in range(3):
            penta()

cikls()

turtle.done()

def uzd(shape, pencolor):
      turtle.showturtle()
      turtle.shape(shape)
      turtle.pencolor(pencolor)
      for x in range(10):
            if x % 2 == 0:
                  turtle.forward(25)
                  turtle.right(45)
            else:
                  turtle.forward(25)
                  turtle.right(45)

uzd("triangle", "red")

turtle.done()

# def spirāle(pencolor):
#       turtle.showturtle()
#       turtle.shape()
#       turtle.pencolor(pencolor)
#       for x in range(2):
#             turtle.forward(20)
#             turtle.right(90)
#       for x in range(2):
#             turtle.forward(40)
#             turtle.right(90)
#       for x in range(2):
#             turtle.forward(60)
#             turtle.right(90)
#       for x in range(2):
#             turtle.forward(80)
#             turtle.right(90)
#       for x in range(2):
#             turtle.forward(100)
#             turtle.right(90)
#       for x in range(2):
#             turtle.forward(120)
#             turtle.right(90)
#       for x in range(2):
#             turtle.forward(140)
#             turtle.right(90)
#       for x in range(2):
#             turtle.forward(160)
#             turtle.right(90)

# spirāle("black")

# turtle.done()