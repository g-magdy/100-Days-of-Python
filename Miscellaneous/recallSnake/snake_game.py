from turtle import Turtle, Screen
from snake import Snake
import time

myScr = Screen()
myScr.setup(width=600, height=600)
myScr.bgcolor("black")
myScr.title("Snake Game! you can exit by pressing s")
myScr.tracer(0)
serpent = Snake()

def close():
    global game_is_on
    game_is_on = False

game_is_on = True

myScr.listen()
myScr.onkey(fun=close, key="s") #do not put parentheses after the function name
myScr.onkey(fun=serpent.goUp, key="Up")
myScr.onkey(fun=serpent.goDown, key="Down")
myScr.onkey(fun= serpent.goLeft, key="Left")
myScr.onkey(fun=serpent.goRight, key="Right")

while game_is_on:
    myScr.update()
    serpent.move()
    time.sleep(0.03)

# this line is better than the exit on click,
# because it does not print strange error messages on the terminal
# when closing the window 
# TODO: I can initiate a sequence to exit the game properly with a message
myScr.bye()