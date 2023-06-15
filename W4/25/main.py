# add each line in weather-data.csv to a list
# # level 0
# with open("weather-data.csv") as weather:
#     data = weather.readlines()

# for i in range(len(data)):
#     data[i] = data[i].strip()

# print(data)

## level 1
# import csv

# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if (row[1] != "temp"):
#             temperatures.append(int(row[1]))
    
# print(temperatures)

import pandas
# data frame is a whole table
# a series is a single column 
data = pandas.read_csv("weather-data.csv")
temp = data["temp"].to_list()
# print(data.temp)
# print(data["temp"].max())

max_t = data["temp"].max()
# print(max_t)
# print(data[data.temp == max_t])

monday = data[data.day == "monday"]
t = int(monday.temp)
print(t * 1.8 + 32)