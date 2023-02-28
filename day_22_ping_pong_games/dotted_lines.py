from turtle import Turtle


class DottedLine(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, -650)
        self.left(90)
        self.draw_dotted_line()

    def draw_dotted_line(self):
        for i in range(70):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
