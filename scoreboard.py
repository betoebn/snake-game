from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.track_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.track_score()

    def track_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", move=False, align="center", font=("Arial", 20, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score} High score: {self.high_score}", move=False, align="center", font=("Arial", 20, "normal"))






