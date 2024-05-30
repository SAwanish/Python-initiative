import turtle
from turtle import Turtle as t, Screen
from random import choice, randint


turtle.colormode(255)

def random_color():
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    colr = (r,g,b)
    return colr

tim = t()
tim.shape("turtle")
tim.speed('fastest')
angle = 0
while angle<360:
    tim.color(random_color())
    tim.circle(90)
    angle +=1
    tim.setheading(angle)
screen = Screen()
screen.exitonclick()