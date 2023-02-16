from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.setup(width=500, height=400)
inp = screen.textinput(title='Make Your Bet', prompt='Which turtle would win the race? Enter a color: ')
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_tim = []
y_pos = [-70, -40, -10, 20, 50, 80]
win = ''


def create_turtles():
    """ Created 6 Turtles"""
    for i in range(6):
        new_turtle = Turtle('turtle')
        new_turtle.color(colors[i])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_pos[i])
        turtle_tim.append(new_turtle)


create_turtles()

if inp:
    is_game_on = True

while is_game_on:
    for turtle in turtle_tim:
        # Make each turtle move a random amount.
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 230:
            win = turtle.pencolor()
            is_game_on = False

if win == inp:
    print(f"You've won! The {win} turtle is the winner!")
else:
    print(f"You've lost! The {win} turtle is the winner!")

screen.exitonclick()
