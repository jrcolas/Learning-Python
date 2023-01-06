

# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

# data = pandas.read_csv("weather_data.csv")
# temperature = data["temp"]
# data_dict = data.to_dict()
# temp_list = temperature.to_list()
#
#
# # avg_temp = sum(temp_list) / len(temp_list)
# avg_temp = temperature.mean()
# max_temp = temperature.max()
# print(max_temp)
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in Row
# print(data[data.day == "Monday"])

# # Day and condition that had the highest temperature
# print(data.temp.max())
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# print(f"Temperature in C: {int(monday.temp)}")
# print(f"Temperature in F: {int(monday.temp) * 1.8 + 32}")

# Creating a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
