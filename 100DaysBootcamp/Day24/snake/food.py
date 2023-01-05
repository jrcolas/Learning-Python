from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.goto(self.randomness())

    def randomness(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        rand_coord = (random_x, random_y)
        return rand_coord

    def refresh(self):
        self.goto(self.randomness())
