from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(location)

    def up(self):
        print("Up is being pressed")
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
