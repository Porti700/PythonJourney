## Carrera de tortugas o Turtle Race


from turtle import Turtle, Screen, screensize
import random

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet =  screen.textinput(title = "Make your Bet", prompt="Which turtle is going to win the race? Enter a color: ")
colors = ["green", "yellow", "orange", "red", "black", "blue"]
names = ["kevin", "mar", "tommy", "tedy", "luis", "rene"]
## Crear las 6 tortugas

for num in range(len(names)):
    (names[num]) = Turtle(shape="turtle")    
    turtles = names[num]
    
# for i in range(len(colors)):
#     num.color(colors[i])

num.penup()
num.goto(x=-230 , y=0)



screen.exitonclick()