import turtle
import pandas
from stateplotter import StatePlotter

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
all_x = data.x.to_list()
all_y = data.y.to_list()

answered_list = []
#states_to_learn = []

while len(answered_list) != 50:
    answer_state = (screen.textinput(title=f"{len(answered_list)}/50 States Correct", prompt="Guess a state below")).title()

    if answer_state == "Exit":
        # # Day 26 List Comprehension Changes
        # for state in all_states:
        #     if state not in answered_list:
        #         states_to_learn.append(state)
        states_to_learn = [state for state in all_states if state not in answered_list]
        stl = pandas.DataFrame(states_to_learn)
        stl.to_csv("states_to_learn.csv")
        break
    if answer_state in answered_list:
        pass
    elif answer_state in all_states:
        i = all_states.index(answer_state)
        guessed_state = answer_state
        guessed_x = all_x[i]
        guessed_y = all_y[i]
        answered_list.append(answer_state)
        sp = StatePlotter(answer_state, guessed_x, guessed_y)
        sp.refresh()
    else:
        pass

# states_to_learn.csv
