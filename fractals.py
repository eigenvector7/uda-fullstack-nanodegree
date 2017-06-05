# -*- coding: utf-8 -*-
""" Standalone implementation of drawing triangular fractals using python turtle library
Uses recursion.

Tested for NUM_LAYERS upto 6.

*USE AT YOUR OWN RISK *
"""
import turtle,time,math

wn = turtle.Screen()
wn.bgcolor("yellow")

MAX_SIZE = 160
NUM_LAYERS = 2

# Utility function to draw a equilateral triangle givern a turtle and lenght of the side
def draw_equitriang(turt,side):
    t.begin_fill()
    t.left(60)
    t.forward(side)
    t.left(120)
    t.forward(side)
    t.left(120)
    t.forward(side)
    t.end_fill()
# Utility function to reset the position of a turtle to provided position and heading
def reset_pos(turt,pos,heading):
    turt.penup()
    turt.setpos(pos)
    turt.setheading(heading)
    turt.pendown()

# For a given turtle and length, draw triangular fractals recursively
def draw_fractal(turt,side,layer)  :
    t = turt
    if layer == 0 :
        #(MAX_SIZE/NUM_LAYERS):
        return
    # Capture the position of the turtle so that we can set it back before returning
    origPos = turt.pos()
    origHead = turt.heading()

    # Draw right side fractal
    t.forward(side/2)
    draw_equitriang(t,side/2)
    t.setheading(origHead)
    draw_fractal(t,side/2,layer-1)
    reset_pos(t, origPos, origHead)
    # Draw left side fractal
    t.backward(side / 2)
    draw_equitriang(t,side/2)
    t.setheading(origHead)
    draw_fractal(t, side / 2,layer-1)
    reset_pos(t, origPos, origHead)

    # Draw fractal above
    reset_pos(t,origPos+(0,(side)*math.cos(math.pi/6)),origHead)
    draw_equitriang(t,side/2)
    t.setheading(origHead)
    draw_fractal(t,side/2,layer-1)
    reset_pos(t,origPos,origHead)


# Basic setup and outer layer drawing
t = turtle.Turtle()
t.shape('turtle')
t.color('blue')
t.speed(3)
oPos = t.pos()
oHead = t.heading()
# PREPOSITION TURTLE TO DRAW OUTER TRIANGLE
t.backward(MAX_SIZE)
t.right(60)
# Draw Outer Triangle
t.fillcolor('cyan')
draw_equitriang(t,MAX_SIZE*2)
# Reposition turtle with original orientation
reset_pos(t, oPos, oHead)
t.fillcolor('white')
# Draw the center triangle
draw_equitriang(t, MAX_SIZE)
reset_pos(t, oPos, oHead)
# Now use recursion to draw it's fractals on right, left and above
draw_fractal(t,MAX_SIZE,NUM_LAYERS)

wn.exitonclick()
