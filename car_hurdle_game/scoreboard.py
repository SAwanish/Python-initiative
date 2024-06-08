from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.initial_level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-210, 250)
        self.write(f'Level : {self.initial_level}', align="center", font=FONT)
    def level(self):
        self.initial_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over!',align="center", font=('courier',40,"normal"))