from turtle import Turtle
ALIGNMENT = 'left'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-290, 260)
        self.update_level()

    def update_level(self):
        self.write(f'Level : {self.level}', align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.home()
        self.write('GAME OVER!', align='center', font=FONT)

    def increment(self):
        self.clear()
        self.level += 1
        self.update_level()