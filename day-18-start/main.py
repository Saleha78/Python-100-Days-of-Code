from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

#timmy.forward(100)
#timmy.left(90)
#timmy.forward(100)
#timmy.left(90)
#timmy.forward(100)

for _ in range(4):
    timmy.left(90)
    timmy.forward(100)


screen = Screen()
screen.exitonclick()

import heroes
print(heroes.gen()) # installed in terminal using pip install heroes