## POO or OOP 
## Clases y objetos en python para POO.

## Create a new object and class
## Object   Class
##  car = CarBlueprint()


## Create a new object with Turtle
## Option 1
# import turtle
# andy =  turtle.Turtle()

##Option 2

# from turtle import Turtle, Screen
# andy = Turtle()
# print(andy)
# andy.shape("turtle")
# andy.color("DarkGray")
# andy.fd(100)

# ## Objects Attributes

# my_screen = Screen()
# print(my_screen.canvheight)

# ## Object Methods
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
