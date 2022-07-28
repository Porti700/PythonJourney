from turtle import Turtle, Screen

tedy = Turtle()
screen = Screen()
 

def move_forward():
    tedy.fd(10)
    
def move_backwards():
    tedy.bk(10)   
    
def move_right():
    tedy.right(10) 
    
def move_left():
    tedy.left(10)     
         
def clear_draw():
    tedy.reset()         

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=clear_draw)
screen.exitonclick()  