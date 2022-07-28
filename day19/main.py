from turtle import Turtle, Screen

tedy = Turtle()
screen = Screen()

def move_forward():
    tedy.fd(10)

screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.exitonclick()    