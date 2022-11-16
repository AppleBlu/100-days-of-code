# Importing modules
import pandas

data = pandas.read_csv('weather_data.csv')

# Collecting data from all columns
temps = data['temp']
conditions = data['condition']
days = data['day']
# Or a simpler way is:
# data.temp etc.

data_dict = data.to_dict()
temp_list = data['temp'].to_list()

# Getting the avg temp
number_of_temps = len(temp_list)
all_temps_added = sum(temp_list)
avg_temp = all_temps_added / number_of_temps
print(avg_temp)

# Simpler way
print(data['temp'].mean())

# Getting max temp
print(data['temp'].max())
