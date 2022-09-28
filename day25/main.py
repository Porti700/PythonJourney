# # Open the weather_data.csv . Use . readlines ( ) to create a list named data that 
# # contains the values from the .csv file .

# from itertools import tee
# import os
# import csv
# # with open("weather_data.csv") as data_file:
# #     data =  data_file.readlines()
# #     print(data)

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(int(row[1]))
#     print(temperature)

from pandas import *
import pandas

data = pandas.read_csv('weather_data.csv')
# print(data)
# print(data['temp'])p

data_dict = data.to_dict()
# print(data_dict)

temp_list = data['temp'].to_list()

## Print the temperature average
## First method
average_temp = sum(temp_list) / len(temp_list)
# print(average_temp.__round__(2))

## Second method
# print(data['temp'].mean())

## Get highest temperature

# print(data['temp'].max())

## Get data in row

# print(data[data.day == 'Monday'])
# print(data)

## Get the row with the highest temperature
max_temp = (data['temp'].max())

# print(data[data.temp == max_temp])

## get value for one day

monday = data[data.day == 'Monday']
# print(monday.temp)
monday_temp = int(monday.temp)
monday_temp_f = 9/5 * monday_temp + 32
# print(monday_temp_f)



## Create a dataframe from scratch

data_dict = {
    "students": ["Kevin", "John", "Amy"],
    "scores": [76,65,74]
}
new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv('new_data.csv')