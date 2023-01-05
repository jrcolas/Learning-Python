import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

# Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

my_turtle = Player()
car0 = CarManager()
car0.hideturtle()
my_score = Scoreboard()
all_cars = []
game_loop = 0


# Make the turtle move
screen.listen()
screen.onkey(my_turtle.up, "Up")
# screen.onkey(my_turtle.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(car0.move_speed)
    screen.update()

    pos_x = 300
    pos_y = random.randint(-250, 250)

    # Reset turtle position when it reaches top
    my_turtle.reset_turtle()

    # Track new level
    # Speed up car after each new level
    if my_turtle.new_level:
        my_score.level_up()
        my_turtle.new_level = False
        car0.move_speed *= 0.9

    # Create cars and make them move
    if game_loop == 6:
        carX = CarManager()
        carX.setpos(pos_x, pos_y)
        all_cars.append(carX)

        game_loop = 0

    for car in all_cars:
        car.move()
        # Detect collision with cars
        if my_turtle.distance(car) < 25:
            my_score.game_over()
            game_is_on = False

    game_loop += 1


screen.exitonclick()
