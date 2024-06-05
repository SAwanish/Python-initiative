from snake import *
from food import *
from scorecard import *

from turtle import Turtle, Screen
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

score = Score()
food = Food()
snake = Snake()
screen.listen()

screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detection of snake collision with the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.calculate_score()

    # Detect collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
        game_is_on = False
        score.game_over()

    # Detect collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()