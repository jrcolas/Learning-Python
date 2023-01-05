from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.color("white")
        self.score = 0
        self.read_hscore()
        self.setposition(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.read_hscore()}", False, align=ALIGNMENT, font= FONT)

    def read_hscore(self):
        with open("data.txt") as data:
            contents = data.read()
        return contents

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > int(self.read_hscore()):
            # self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_score()
