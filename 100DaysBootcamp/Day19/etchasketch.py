import turtle as t

cursor = t.Turtle()
screen = t.Screen()


def move_forwards():
    cursor.forward(5)


def move_backwards():
    cursor.backward(5)


def clockwise():
    cursor.left(5)


def counter_clockwise():
    cursor.right(5)


def reset_cursor():
    screen.reset()
    cursor.reset()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=reset_cursor)
screen.exitonclick()
