from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shapesize(stretch_len= 0.5, stretch_wid = 0.5) # 10*10 size
        self.shape("circle")
        self.color("green")
        self.speed("fastest")
        self.penup()
        self.gotoRandPos()
        
    def gotoRandPos(self):
        randX = randint(-280, 280)
        randY = randint(-280, 280)
        self.goto(randX, randY )