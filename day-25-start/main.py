import pandas

# with open("weather_data.csv") as file:
# #     data = file.readlines()
# #     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(len(temp_list))
# #
# # avg_temp = sum(temp_list) / len(temp_list)
# # print(avg_temp)
# #
# # # OR
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
# #
# # # Get data in columns
# # print(data["condition"])
# # print(data.condition)
#
# # Get Data in Row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 1.8 +32
# print(monday_temp_F)

# Create dataframe from scratch
# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

fur_colors = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrel_count, black_squirrel_count, cinnamon_squirrel_count]
}

squirrel_count = pandas.DataFrame(fur_colors)
squirrel_count.to_csv("squirrel_count.csv")
