from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore=0
        self.penup()
        self.color("white")
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score:{self.score} highscore:{self.highscore}', align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
        self.score=0
        self.update_score()
    def is_game_over(self):
        self.goto(0,0)
        self.write(f'GameOver', align="center", font=("Arial", 24, "normal"))

