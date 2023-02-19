from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f'Score : {self.score}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write('GAME OVER!', align=ALIGNMENT, font=FONT)

    def increment(self):
        self.clear()
        self.score += 1
        self.update_score()
