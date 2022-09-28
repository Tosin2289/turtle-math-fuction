import turtle
import math
import random

t=turtle.Turtle()
t.speed(100)
t.color("green","black")

t.begin_fill()
for i in range(200):
    t.forward(math.sin(i/10)*30)
    t.right(20)

t.end_fill()

turtle.done()