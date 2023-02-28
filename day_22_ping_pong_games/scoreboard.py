from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 60, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.goto(0, 270)
        self.color("white")
        self.score_update()

    def score_update(self):
        self.goto(-100,200)
        self.write(f'{self.l_score}', align='left', font=FONT)
        self.goto(100, 200)
        self.write(f'{self.r_score}', align='right', font=FONT)

    def increment_l(self):
        self.clear()
        self.l_score += 1
        self.score_update()

    def increment_r(self):
        self.clear()
        self.r_score += 1
        self.score_update()