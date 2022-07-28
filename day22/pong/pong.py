from turtle import Screen, Turtle

## Crear la pantalla del juego

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)



## Create two paddles with a width:20 and height:100, x_position= 350, y_position= 0

paddle_1 = Turtle()
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(x=350, y=0)



def go_up():
    new_y = paddle_1.ycor() + 20
    paddle_1.goto(paddle_1.xcor() , new_y)
    
def go_down():
    new_y = paddle_1.ycor() - 20
    paddle_1.goto(paddle_1.xcor() , new_y)    
    
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")



game_is_on = True
while game_is_on:
    screen.update()


    
screen.exitonclick()
Screen.exitonclick()