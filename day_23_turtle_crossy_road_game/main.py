import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title('Turtle Crossy Road')
screen.tracer(0)


player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(fun=player.move_turtle, key='Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    # Detect if the turtle has collided with the cars

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()



    # Detect if the turtle has crossed successfully
    if player.is_at_finish_line():
        player.go_to_start_position()
        cars.level_up()
        score.increment()

screen.exitonclick()
