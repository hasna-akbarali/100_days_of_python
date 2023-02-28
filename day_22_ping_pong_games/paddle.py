from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.setpos(pos)
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()

    def go_up(self):
        if self.ycor() < 300 or self.ycor() > -300:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() < 300 or self.ycor() > -300:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
