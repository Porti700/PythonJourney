from cgitb import grey
import pandas
from pandas import *



data = pandas.read_csv('squirrel_data.csv')
# print(data)

grey_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])

print(grey_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_list = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_list)
df.to_csv('squirrel_count.csv')

print(df)
