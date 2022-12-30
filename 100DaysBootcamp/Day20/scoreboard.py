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
        self.setposition(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("HA HA... NOOB", False, align=ALIGNMENT, font= FONT)