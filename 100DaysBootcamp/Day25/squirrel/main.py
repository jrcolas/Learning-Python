import pandas

data = pandas.read_csv("squirrel_census.csv")

colors = data["Primary Fur Color"]
s_gray = data[colors == "Gray"]
s_cinnamon = data[colors == "Cinnamon"]
s_black = data[colors == "Black"]

color_dict = {
    "colors": ["Gray", "Cinnamon", "Black"],
    "count": [len(s_gray), len(s_cinnamon), len(s_black)]
}

custom_table = pandas.DataFrame(color_dict)
custom_table.to_csv("squirrel_count.csv")
