from turtle import Turtle
ALIGNMENT = "center"
FONT = "Courier", 20, "normal"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.update_scoreboard()
        self.score = 0

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High score : {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    # def lose(self):
    #     self.clear()
    #     self.color("red")
    #     self.goto(0, 0)
    #     self.write(arg=f"👽 GAME OVER! Final score: {self.score} 👽 ", align=ALIGNMENT, font=FONT)
