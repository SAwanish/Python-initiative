from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make Your Bet', prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
j = -120
for colr in colors:
    j += 40
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colr)
    new_turtle.penup()
    new_turtle.goto(x=-230, y= j)
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_dist = randint(0,10)
        turtle.forward(rand_dist)
        if turtle.xcor() > 230:
            is_race_on = False
            win_color = turtle.pencolor()
            if  win_color == user_bet:
                print(f"You've won! The {win_color} turtle is the winner.")
            else:
                print(f"You've lost! The {win_color} turtle is the winner.")

screen.exitonclick()