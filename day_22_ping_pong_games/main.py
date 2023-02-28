from turtle import Screen
import time
from ball import Ball
from dotted_lines import DottedLine
from paddle import Paddle
from scoreboard import ScoreBoard

COLLISION_DISTANCE = 50

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Ping Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
# dotted_lines = DottedLine()
score = ScoreBoard()

screen.listen()
screen.onkeypress(fun=r_paddle.go_up, key='Up')
screen.onkeypress(fun=r_paddle.go_down, key='Down')
screen.onkeypress(fun=l_paddle.go_up, key='w')
screen.onkeypress(fun=l_paddle.go_down, key='s')

game_is_on = True
while game_is_on:
    ball.move()
    time.sleep(ball.game_speed)

    # Detect collision with the wall and bounce
    if 280 < ball.ycor() or ball.ycor() < -280:
        print('bouncing')
        ball.bounce_y()
        ball.move()

    # Detect collision with the right paddle
    if ball.distance(r_paddle) < COLLISION_DISTANCE and ball.xcor() > 320:
        ball.bounce_x()
        ball.move()
        score.increment_r()
        print('r_paddle hits!')

    # If the right paddle misses
    elif ball.xcor() > 380:
        score.increment_l()
        ball.reset()

    # Detect collision with the left paddle
    if ball.distance(l_paddle) < COLLISION_DISTANCE and ball.xcor() < -320:
        ball.bounce_x()
        ball.move()
        score.increment_l()
        print('l_paddle hits!')


    # If the left paddle misses
    elif ball.xcor() > 380:
        score.increment_r()
        ball.reset()

    screen.update()


screen.exitonclick()