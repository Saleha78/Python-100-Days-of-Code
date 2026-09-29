from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.backward(50)
    tim.right(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.forward(50)
    tim.right(90)
    tim.forward(50)
screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()