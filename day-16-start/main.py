
import turtle                       #from turtle import Turtle,Screen
imy = turtle.Turtle()                # imy = Turtle()
imy.color("green")
imy.shape("turtle")
imy.speed(1)
imy.forward(100)
imy.left(90)
imy.forward(100)
imy.left(90)
imy.forward(100)
imy.left(90)
imy.forward(100)
imy.forward(200)
imy.right(90)
imy.forward(100)
imy.right(90)
imy.forward(300)

my_screen = turtle.Screen()          # my_screen = Screen
print(my_screen.canvheight)
my_screen.exitonclick()
