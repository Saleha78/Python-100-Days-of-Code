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

pen.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range (int(360/size_of_gap)):
        pen.color(random_color())
        pen.circle(180)
        pen.setheading(pen.heading() + size_of_gap)
draw_spirograph(5)


# for _ in range(100):
#         pen.color(random_color())
#         pen.circle(180)
#         pen.left(10)




screen.exitonclick()