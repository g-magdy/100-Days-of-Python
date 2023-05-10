from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.speed("fastest")
        self.color("#02b3e4")
        self.shape("circle")
        self.newPos()
        
    def newPos(self):
        self.hideturtle()
        self.goto(random.randint(-250, 250), random.randint(-250, 250))
        self.showturtle()