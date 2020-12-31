#Open the weather_data.csv. Use .readlines() to create a list named data that contains the values from the .csv file.

# with open("weather_data.csv") as data_file:
# 	data = data_file.readlines()
# 	print(data)

# import csv

# with open("weather_data.csv") as data_file:
# 	data = csv.reader(data_file)
# 	temparatures = []
# 	for row in data:
# 		if row[1] != "temp":
# 			temparatures.append(int(row[1]))
# 	print(temparatures)

# with open("weather_data.csv") as data_file:
# 	data = data_file.readlines()
# 	print(data)


import csv


with open("weather_data.csv") as data_file:
	data = csv.reader(data_file)
	temperatures = []
	for row in data:
		if row[1] != "temp":
			temperatures.append(row[1])
	print(temperatures)