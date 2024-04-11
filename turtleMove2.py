
import turtle 
  
screen = turtle.Screen() 
screen.setup(500,500) 
screen.bgcolor('Green')   
screen.tracer(0)             
  
t = turtle.Turtle() 
t.speed(0) 
t.width(3) 
  
t.hideturtle()             
  
def draw_penta() : 
    t.fillcolor("Orange") 
    t.begin_fill() 
    for i in range(5) : 
        t.forward(100) 
        t.left(72) 
    t.end_fill() 
    t.speed(7)
t.penup() 
t.goto(-350, 0) 
t.pendown() 

def lol():
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(1):
        t.circle(60)
    t.end_fill()
    t.speed(5)
t.penup() 
t.goto(-300, 0) 
t.pendown() 
  
while True : 
    t.clear() 
    draw_penta() 
    lol()
      
    screen.update()          
    t.forward(0.05) 
