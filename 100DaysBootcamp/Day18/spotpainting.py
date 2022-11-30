# import colorgram
#
# colors = colorgram.extract("dots.jpg", 15)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgbs = (r, g, b)
#     rgb_colors.append(rgbs)
#
# print(rgb_colors)

import turtle as t
import random


brush = t.Turtle()
color_list = [(232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165)]
t.colormode(255)

brush.penup()
brush.setpos(-300, -300)

row = 0
xp = -300
yp = -300

while row != 10:
    for _ in range(10):
        brush.dot(30, random.choice(color_list))
        brush.forward(60)
    yp += 60
    brush.setpos(xp, yp)
    row += 1


screen = t.Screen()
screen.exitonclick()