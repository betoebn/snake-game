from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.track_score()

    def track_score(self):
        self.clear()
        self.write(f"Score: {self.score}", move=False, align="center", font=("Arial", 20, "normal"))
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over! Your score is: {self.score - 1}", move=False, align="center", font=("Arial", 20, "normal"))
