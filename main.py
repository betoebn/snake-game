from turtle import Screen
from snake import Snake
from food import Food
import time

# Screen setup to 600px to 600px with black background
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake v0.1")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(snake.left, "Left")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()













