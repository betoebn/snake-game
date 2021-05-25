from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

difficulty = 0.07
# Screen setup to 600px to 600px with black background
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake v0.1")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

head = snake.segments[0]
screen.listen()
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(difficulty)
    snake.move()
    if snake.segments[0].distance(food) < 20:
        food.new_food()
        snake.extend()
        scoreboard.track_score()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() < -290 or head.ycor() > 290:
        scoreboard.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
