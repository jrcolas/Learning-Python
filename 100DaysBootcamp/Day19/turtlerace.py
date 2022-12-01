import turtle
from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-125, -75, -25, 25, 75, 125]

all_turtles = []
is_race_on = False

if user_bet:
    is_race_on = True

for turtle_index in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(-230, y_pos[turtle_index])
    all_turtles.append(tim)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won! The {turtle.pencolor()} turtle won the race!")
            else:
                print(f"You lost! The {turtle.pencolor()} turtle won the race!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
