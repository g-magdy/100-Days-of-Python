import info_and_prams as const
from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(const.SCORE_COLOR)
        self.goto(- const.SCREEN_SIDE//2 + 30, const.SCREEN_SIDE//2 -40)
        self.level = 0
        self.showLevel()
        
        
    def showLevel(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=const.FONT)
        
    def levelUp(self):
        self.level += 1
        
    def gameOver(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"    Game over\nyou reached level {self.level}", font=const.FONT, align="center")