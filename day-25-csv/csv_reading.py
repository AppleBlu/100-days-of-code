# Importing modules
import pandas

data = pandas.read_csv('weather_data.csv')
temps = data['temp']

print(data)
print(temps)
