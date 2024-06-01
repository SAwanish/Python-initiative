from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        self.score = 0
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.calculate_score()

    def update_score(self):
        self.write(f"Score = {self.score}", False, align="center", font=("Courier", 24, "normal"))

    def calculate_score(self):
        self.clear()
        self.update_score()
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 24, "normal"))