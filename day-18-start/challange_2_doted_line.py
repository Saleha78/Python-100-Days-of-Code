from turtle import Turtle,Screen

turtle = Turtle()
turtle.shape("arrow")

for _ in range(50):

    turtle.pendown()
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)



screen = Screen()
screen.exitonclick()
