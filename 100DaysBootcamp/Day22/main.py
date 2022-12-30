import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


# Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)


def move_paddle(paddle, up, down):
    screen.listen()
    screen.onkey(paddle.up, up)
    screen.onkey(paddle.down, down)


# Create and move a paddle
l_paddle = Paddle((-350, 0))
move_paddle(l_paddle, "w", "s")

# Create another paddle
r_paddle = Paddle((350, 0))
move_paddle(r_paddle, "Up", "Down")

# Create the ball and make it move
ball = Ball()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    # Detect collision with wall and bounce
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # Detect collision with paddles
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect when r_paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when l_paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


# Exit on click
screen.exitonclick()
