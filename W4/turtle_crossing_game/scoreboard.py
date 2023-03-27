from turtle import Turtle

FONT = ("InputMono", 16, "bold")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setpos(x=-290, y=270)
        self.level = 1 # initially 
    
    def viewScore(self):
        self.clear()
        self.write(f"Level = {self.level}",  font=FONT)
    
    def incremetScore(self):
        self.level += 1
        
    def endgame(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over, your score is {self.level}", align="center", font=FONT)