from turtle import Screen
import time

from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkeypress(fun=snake.go_up, key="Up")
screen.onkeypress(fun=snake.go_down, key="Down")
screen.onkeypress(fun=snake.go_right, key="Right")
screen.onkeypress(fun=snake.go_left, key="Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increment()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 \
            or 280 < snake.head.ycor() or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with snake
    # if head collides with a segment in the tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
