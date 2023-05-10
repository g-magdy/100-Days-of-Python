from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

myScr = Screen()
myScr.setup(width=600, height=600)
myScr.bgcolor("black")
myScr.title("Snake Game! you can exit by pressing s")
myScr.tracer(0)
serpent = Snake()
myFood = Food()
judge = Scoreboard()

def exitLoop():
    global game_is_on
    game_is_on = False

game_is_on = True

myScr.listen()
myScr.onkey(fun=exitLoop, key="e") #do not put parentheses after the function name
myScr.onkey(fun=serpent.goUp, key="Up")
myScr.onkey(fun=serpent.goDown, key="Down")
myScr.onkey(fun= serpent.goLeft, key="Left")
myScr.onkey(fun=serpent.goRight, key="Right")

while game_is_on:
    judge.showScore()
    myScr.update()
    serpent.move()
    if serpent.eatFood(myFood):
        serpent.grow()
        judge.incrementScore()
    game_is_on = not serpent.collision()
    time.sleep(0.03)

#myScr.bye()
# this line is better than the exit on click,
# because it does not print strange error messages on the terminal
# when closing the window 
judge.gameOver()
myScr.exitonclick()