from turtle import Turtle,Screen
tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_left():
    tim.left(10)
    #OR
    # new_heading = tim.heading() + 10
    # tim.setheading(new_heading)
def move_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



screen.listen()

screen.onkeypress(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_left, "d")
screen.onkey(move_right, "a")
screen.onkey(clear, "c")


screen.exitonclick()