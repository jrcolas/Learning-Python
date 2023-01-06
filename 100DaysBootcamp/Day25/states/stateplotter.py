from turtle import Turtle

FONT = ("Arial", 8, "normal")


class StatePlotter(Turtle):
    def __init__(self, s, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.state = s
        self.speed("fastest")
        # self.write(f"{state}", False, font=FONT)
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"{self.state}", False, font=FONT)
