from turtle import Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("PONG")
screen.bgcolor("white")
screen.setup(width=800, height=600)
ball = Ball()
screen.tracer(0)
scoreboard = Scoreboard()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()

screen.onkey(fun=r_paddle.up, key="Up")
screen.onkey(fun=r_paddle.down, key="Down")

screen.onkey(fun=l_paddle.up, key="w")
screen.onkey(fun=l_paddle.down, key="s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
