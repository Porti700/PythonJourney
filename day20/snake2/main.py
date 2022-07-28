from  turtle import Turtle, Screen, color

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


## forma 1 de crear los cuadrados con ciclo for y lista de posiciones

starting_positions = [(0,0), (-20,0), (20,0)]

segments = []
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


game_is_on = True
while game_is_on:
    for seg in segments:
        seg.fd(20)


screen.exitonclick()

