# # Importing modules
import pandas
#
# data = pandas.read_csv('weather_data.csv')
#
# # Collecting data from all columns
# temps = data['temp']
# conditions = data['condition']
# days = data['day']
# # Or a simpler way is:
# # data.temp etc.
#
# data_dict = data.to_dict()
# temp_list = data['temp'].to_list()
#
# # Getting the avg temp
# number_of_temps = len(temp_list)
# all_temps_added = sum(temp_list)
# avg_temp = all_temps_added / number_of_temps
#
# # Simpler way
# avg_temp_2 = data['temp'].mean()
#
# # Getting max temp
# max_temp = data['temp'].max()
#
# # Data in row
# monday_data = data[data.day == 'Monday']
# max_temp_data_row = data[data.temp == max_temp]
#
# monday_condition = monday_data.condition
# monday_temp_c = int(monday_data.temp)
# monday_temp_f = monday_temp_c * 9/5 + 32
#
# # Creating mainframe
# student_scores = {
#     'students': ['ben', 'max', 'sam'],
#     'scores': [32, 42, 12]
# }
#
# new_data = pandas.DataFrame(student_scores)
# new_data.to_csv('new_data_csv.csv')


squiral_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
print(squiral_data)
squiral_data = pandas.DataFrame(squiral_data)

squiral_data.to_csv('squiral_data.csv')
