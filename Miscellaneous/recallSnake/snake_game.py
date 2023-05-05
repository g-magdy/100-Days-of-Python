from turtle import Turtle, Screen
from snake import Snake
import time

myScr = Screen()
myScr.setup(width=600, height=600)
myScr.bgcolor("black")
myScr.title("This is the snake Game! you can exit by pressing e or clicking the screen")
myScr.tracer(0)
serpent = Snake()

myScr.listen()
myScr.onkey(fun=myScr.bye, key="e") #PLEASE do not put parentheses here
myScr.onkey(fun=serpent.goUp, key="Up")
myScr.onkey(fun=serpent.goDown, key="Down")
myScr.onkey(fun= serpent.goLeft, key="Left")
myScr.onkey(fun=serpent.goRight, key="Right")

game_is_on = True
while game_is_on:
    serpent.move()
    myScr.update()
    time.sleep(0.03)

myScr.exitonclick()