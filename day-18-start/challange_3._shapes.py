from turtle import Turtle, Screen
import random
tim = Turtle()

colors = ["red", "green", "blue", "yellow", "cyan", "magenta"]

# sides = (3,4, 5, 6, 7, 8, 9)
# for side in sides:
#     angle = 360 / side
#     for _ in range(side):
#         tim.forward(100)
#         tim.left(angle)


def draw_shapes(num_of_sides):
        angle = 360 / num_of_sides
        for _ in range(num_of_sides):
            tim.forward(100)
            tim.left(angle)
for shapes_side_n in range(3,11):
    tim.color(random.choice(colors))
    draw_shapes(shapes_side_n)





screen = Screen()
screen.exitonclick()