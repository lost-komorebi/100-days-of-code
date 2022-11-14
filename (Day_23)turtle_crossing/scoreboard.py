from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 1
        self.update_score()

    def update_score(self):
        self.penup()
        self.color('black')
        self.hideturtle()
        self.clear()
        self.goto(-235, 270)
        self.write(f'Level: {self.score}', align='center', font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)
