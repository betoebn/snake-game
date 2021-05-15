from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.segments[0].forward(MOVE)

    def up(self):
        if self.orientation() != DOWN:
            self.segments[0].setheading(UP)

    def down(self):
        if self.orientation() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.orientation() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.orientation() != LEFT:
            self.segments[0].setheading(RIGHT)



