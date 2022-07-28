from pydoc import TextDoc
from turtle import Screen, Turtle

## Forma de importar modulos en py

# from turtle import Turtle
# from turtle import *
# import turtle as t                     Crea un alias con el nombre del modulo para poder usarlo despues

# import heroes
# print(heroes.gen())
## Crear un nuevo objeto en la clase Tortuga, objeto se llamara teddy_the_turtle

tedy = Turtle()
tedy.shape("turtle")

for i in range(15):
    tedy.fd(10)
    tedy.penup()
    tedy.fd(10)
    tedy.pendown()
    
    


        
    
    
    

screen = Screen()
screen.exitonclick()

