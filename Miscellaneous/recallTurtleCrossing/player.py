from turtle import Turtle
import info_and_prams as const

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.penup()
        self.goto(const.STARTING_POS)
        self.seth(90)
        
    def moveUp(self):
        self.fd(const.PLAYER_STEP_SIZE)
        
    def passedFinishLine(self):
        if (self.ycor() > const.SCREEN_SIDE//2 - 10):
            return True
        else:
            return False
    def resetPos(self):
        self.goto(const.STARTING_POS)