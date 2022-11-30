import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)
#timmy.shape("turtle")
#timmy.color("chartreuse2")

# Drawing a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Drawing a dashed line
# for _ in range(15):
#     timmy.pd()
#     timmy.forward(10)
#     timmy.pu()
#     timmy.forward(10)


SIDES = 10
COLORS = ["red", "blue", "green", "orange", "brown", "aqua", "purple", "pink", "cyan", "yellow"]
DIRECTIONS = [0, 90, 180, 270]


# Drawing different shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape in range(3, SIDES):
#     timmy.color(random.choice(COLORS))
#     draw_shape(shape)

# Drawing random lines in random directions
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


# timmy.pensize(10)
timmy.speed("fastest")
#
# for _ in range(250):
#     timmy.color(random_color())
#     timmy.setheading(random.choice(DIRECTIONS))
#     timmy.forward(20)


# Drawing a circle thingy
def draw_spirograph(gap_size):
    for _ in range(int(360/gap_size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)
        

draw_spirograph(5)
screen = turtle.Screen()
screen.exitonclick()
