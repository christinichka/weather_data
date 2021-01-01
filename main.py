# Open the weather_data.csv. Use .readlines() to create a list named data that contains the values from the .csv file.

with open("weather_data.csv") as data_file:
	data = data_file.readlines()
	print(data)

import csv

with open("weather_data.csv") as data_file:
	data = csv.reader(data_file)
	temparatures = []
	for row in data:
		if row[1] != "temp":
			temparatures.append(int(row[1]))
	print(temparatures)

with open("weather_data.csv") as data_file:
	data = data_file.readlines()
	print(data)


import csv

with open("weather_data.csv") as data_file:
	data = csv.reader(data_file)
	temperatures = []
	for row in data:
		if row[1] != "temp":
			temperatures.append(row[1])
	print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

#One way to find the average temperature
average = sum(temp_list) / len(temp_list)
print(average)

#Another way to find the average temperature using the mean function in Pandas
print(data["temp"].mean())

#Maximum value of the temperature from the data series
print(data["temp"].max())

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)

#Monday temperature converted from Celsius to Faranheit
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

