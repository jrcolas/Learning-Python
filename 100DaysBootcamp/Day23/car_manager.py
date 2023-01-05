from turtle import Turtle

import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

RANDOM_X = random.randint(-300, 300)
RANDOM_Y = random.randint(-230, 230)


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setpos(RANDOM_X, RANDOM_Y)
        self.x_move = MOVE_INCREMENT
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() - self.x_move
        self.goto(new_x, self.ycor())
