from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.setpos(0, 260)
        self.score = 0
        self.highScore = 0
        
    def showScore(self):
        self.clear()
        self.write(arg=f"Score: {self.score} HighScore: {self.highScore}", align="center", font=("Courier", 20, "normal"))
        
    def incrementScore(self):
        self.score += 1
        
    def resetScore(self):
        if (self.score > self.highScore):
            self.highScore = self.score
        self.score = 0
        self.showScore()
        
    # def gameOver(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(arg=f"  Game Over\nFinal Score = {self.score}", align="center", font=("Courier", 22, "normal"))