# Importing modules
import csv
import pandas

# with open(file='weather_data.csv') as weather_data:
#     weather_data_lst = weather_data.readlines()
#     print(weather_data_lst)

with open(file='weather_data.csv') as weather_data:
    data = csv.reader(weather_data)
    temperatures = []
    for row in data:
        print(row)
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    print(temperatures)
