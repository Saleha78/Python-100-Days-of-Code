from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((380,0))
l_paddle = Paddle((-380,0))
ball = Ball()
scoreboard = Scoreboard()

scoreboard.update_score()
line = Turtle()
line.hideturtle()
line.color("white")
line.penup()
line.goto(0,380)
line.pendown()
line.goto(0,-380)


screen.listen()
screen.onkeypress(r_paddle.up,"Up")
screen.onkeypress(r_paddle.down,"Down")
screen.onkeypress(l_paddle.up,"w")
screen.onkeypress(l_paddle.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 290  or ball.ycor() < -290:
        ball.y_bounce()

    #to detect collision with r_paddle
    # if ball.distance(r_paddle) < 50 and ball.xcor() > -380:
    #     ball.x_bounce()
    #to detect collision with both paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > -320 or ball.distance(l_paddle) < 50 and ball.xcor() < 320:
        ball.x_bounce()
    #detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if  ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()







screen.exitonclick()
