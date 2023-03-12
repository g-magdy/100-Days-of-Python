from turtle import Turtle

ALIGNMENT = "center"
NAME = "InputMono"
SIZE = 18
TYPE = "normal"
COLOR = "white"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setposition(0, 260)
        self.score = 0
        self.display()
        
    def display(self):
        self.clear()
        self.color(COLOR) # IF YOU WANT TO CHANGE THE FONT COLOR
        self.write(f"Score = {self.score}", align= ALIGNMENT, font=(NAME, SIZE, TYPE))
        
