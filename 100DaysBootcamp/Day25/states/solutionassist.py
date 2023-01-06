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
answered_list = []

while len(answered_list) < 50:
    answer_state = (screen.textinput(title=f"{len(answered_list)}/50 States Correct",
                                     prompt="Guess a state below")).title()
    if answer_state == "Exit":
        break
    if answer_state in answered_list:
        pass
    elif answer_state in all_states:
        guessed_state = answer_state
        state_data = data[data.state == answer_state]
        answered_list.append(answer_state)
        sp = StatePlotter(state_data.state.item(), int(state_data.x), int(state_data.y))
        sp.refresh()
    else:
        pass



