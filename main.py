# with open("weather-data.csv") as file:
#     data = file.readlines()
#     print(data)
#

# import csv
#
# with open("weather-data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas
data = pandas.read_csv("weather-data.csv")
data_list = data["temp"].to_list()
# total = 0
# for num in data_list:
#     total += num
#
# print(total)
# print(total / len(data_list))

# print(sum(data.temp)/len(data.temp))
# print(data.temp.mean())

# print(data[data.temp.max() == data.temp])


# bad = "rice",3,"beans"
# sq = pandas.DataFrame(bad)
# sq.to_csv("new_sq.csv")


style = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

b_num = len(style[style["Primary Fur Color"] == "Black"])
red_num = len(style[style["Primary Fur Color"] == "Cinnamon"])
gray_num = len(style[style["Primary Fur Color"] == "Gray"])
# print(b_num)
# print(red_num)
# print(gray_num)

data = {
    "fur_color": ["gray", "red", "black"],
    "number": [gray_num, red_num, b_num]
}
new_table = pandas.DataFrame(data)
new_table.to_csv("sq_count")


# OR OR OR


style = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

fur_color_counts = style["Primary Fur Color"].value_counts()

data = {
    "fur_color": fur_color_counts.index,
    "number": fur_color_counts.values
}
new_table = pandas.DataFrame(data)
new_table.to_csv("new_sq_count")
