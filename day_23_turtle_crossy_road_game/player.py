from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start_position()
        self.setheading(90)

    def move_turtle(self):
        self.forward(distance=MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > 280:
            return True
        return False

    def go_to_start_position(self):
        self.goto(STARTING_POSITION)