from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

myScr = Screen()
myScr.setup(width=600, height=600)
myScr.bgcolor("black")
myScr.title("Snake Game! you can exit by pressing e then q")
myScr.tracer(0)
serpent = Snake()
myFood = Food()
judge = Scoreboard()

game_is_on = True

def exitLoop():
    global game_is_on
    game_is_on = False

def quitGameProperly():
    global game_is_on
    if (not game_is_on):
        myScr.bye()
        

myScr.listen()
myScr.onkey(fun=exitLoop, key="e") #do not put parentheses after the function name
myScr.onkey(fun=quitGameProperly, key="q")
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
    if serpent.collision():
        judge.resetScore()
        serpent.resetSnake()
    time.sleep(0.03)

# judge.gameOver()
myScr.exitonclick()