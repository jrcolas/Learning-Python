from snake import Snake
import time
from turtle import Screen
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Best Snake Game")

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # TODO Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()


    # TODO Create a scoreboard

# TODO Detect collision with wall
# TODO Detect collision with tail


screen.exitonclick()
