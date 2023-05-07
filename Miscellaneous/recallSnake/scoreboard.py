from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 260)
        self.score = 0
        
    def showScore(self):
        self.clear()
        self.write(arg=f"Score = {self.score}", align="center", font=("Arial", 20, "normal"))
        
    def incrementScore(self):
        self.score += 1