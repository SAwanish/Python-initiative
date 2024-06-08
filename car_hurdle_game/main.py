import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
car_manager = CarManager()
screen.listen()

screen.onkeypress(player.go_up,'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detection of finish line
    if player.ycor() > 280:
        player.re_begin()
        score.level()
        car_manager.level_up()

    # Detection with the car
    for car in car_manager.all_cars:
        if car.distance(player)< 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()