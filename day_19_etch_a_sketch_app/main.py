from turtle import Turtle, Screen
tim = Turtle()


def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_clockwise():
    new_heading = tim.heading()
    tim.setheading(new_heading +10)

def move_anticlockwise():
    new_heading = tim.heading()
    tim.setheading(new_heading - 10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

my_screen = Screen()
my_screen.listen()
my_screen.onkey(key="w", fun=move_forwards)
my_screen.onkey(key="s", fun=move_backwards)
my_screen.onkey(key="a", fun=move_clockwise)
my_screen.onkey(key="d", fun=move_anticlockwise)
my_screen.onkey(key="c", fun=clear_screen)
my_screen.exitonclick()
