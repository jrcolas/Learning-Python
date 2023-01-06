import turtle
import pandas
from stateplotter import StatePlotter

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# # Getting state coordinate values from mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

# Data frame that will be plotted on the map
plotted_dict = {
    "state": [],
    "x": [],
    "y": []
}

us_states = pandas.read_csv("50_states.csv")

NUMBER_STATES = 50
score = 0
state_name = ""
state_x = 0
state_y = 0
tracking_list = []

while score != NUMBER_STATES:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="Type a State's Name")
    search_word = answer_state.title()
    result = us_states[us_states.state == search_word]

    if result.empty:
        print("Data not found")
    else:
        if search_word.title() in tracking_list:
            pass
        else:
            tracking_list.append(search_word)
            score += 1

            plotted_dict["state"].append(search_word)
            plotted_dict["x"].append(int(result.x.to_string(index=False)))
            plotted_dict["y"].append(int(result.y.to_string(index=False)))

            plotted_data = pandas.DataFrame(plotted_dict)

            for i in range(plotted_data.state.count()):
                state_name = (plotted_data.state[plotted_data.index == i]).to_string(index=False)
                state_x = int(plotted_data.x[plotted_data.index == i])
                state_y = int(plotted_data.y[plotted_data.index == i])

            paste_state = StatePlotter(state_name, state_x, state_y)
            paste_state.refresh()
