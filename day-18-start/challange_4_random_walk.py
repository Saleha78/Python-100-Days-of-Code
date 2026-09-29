from turtle import Turtle, Screen
import random
screen = Screen()

pen = Turtle()
screen.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
angle = [0,90,180,270]
pen.pensize(10)
pen.speed(15)
for _ in range(200):

    pen.color(random_color())
    pen.forward(30)
    pen.setheading(random.choice(angle))


screen.exitonclick()




# 🐢 setheading() — Perfect Definition
#
# setheading(angle) sets the turtle's direction to an exact angle, regardless of which direction the turtle was facing before.
#
# In simple English:
#
# "Turtle, stop caring about your current direction and face this exact direction."