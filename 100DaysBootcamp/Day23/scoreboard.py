from turtle import Turtle
from player import Player

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.setpos(-280, 250)
        self.write(f"Level: {self.level}", False, font=FONT)

    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)
