from turtle import Turtle

FONT = ("Arial", 30, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(0, 250)
        self.l_score = 0
        self.r_score = 0
    
    def rightSores(self):
        self.r_score += 1
        
    def leftScores(self):
        self.l_score += 1
        
    def displayScore(self):
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align="center", font= FONT)