import turtle,time
from random import randint
wn = turtle.Screen()
wn.bgcolor("yellow")
def draw_square(length):

    s = turtle.Turtle()
    for i in range(4):
        s.forward(100)
        s.right(90)

def draw_circle(turt,radius):
    c = turt
    c.shape('arrow')
    c.color('green')
    c.circle(radius)

def draw_rhombus(turt,side)  :
    t = turt
    t.speed(10)
#    t.right(15)
    t.forward(100)
    t.right(45)
    t.forward(100)
    t.right(135)
    t.forward(100)
    t.right(45)
    t.forward(100)

t = turtle.Turtle()
t.shape('turtle')
t.color('blue')
for i in range(100):
    draw_rhombus(t,100)
    t.right(10)
t.home()
t.right(90)
t.forward(300)


wn.exitonclick()
