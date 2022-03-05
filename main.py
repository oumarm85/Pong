from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

game_is_on = True

rt_paddle = Paddle((350, 0))
lt_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.onkeypress(rt_paddle.paddle_up, "Up")
screen.onkeypress(rt_paddle.paddle_down, "Down")
screen.onkeypress(lt_paddle.paddle_up, "w")
screen.onkeypress(lt_paddle.paddle_down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    screen.listen()
    ball.move()

    # ball has hit a walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # ball has made contact with paddle
    if ball.distance(rt_paddle) < 50 and ball.xcor() > 320 or ball.distance(lt_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #rt paddle misses ball
    if ball.xcor() > 480:
        ball.miss()
        score.l_point()

    #lt paddle missed ball
    if ball.xcor() < -480:
        ball.miss()
        score.r_point()

screen.exitonclick()