from turtle import Turtle
FONT = ("Courier", 16, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level = 0
        self.goto(-238, 270)
        self.score_leve()

    def score_leve(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER 😂", align=ALIGNMENT, font=FONT)



