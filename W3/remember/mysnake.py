import turtle
import time # IMPORTANT
from snake import Snake
from food import Food
from scoreboard import Scoreboard
playground = turtle.Screen()
playground.setup(width=600, height=600)
playground.bgcolor("Black")
playground.title("My Snake Game")
playground.tracer(0)

gorg = Snake()
akly = Food()
board = Scoreboard()

playground.listen()
playground.onkey(key="Up", fun= gorg.up) # type the name of the function without the ()
playground.onkey(key="Down", fun=gorg.down)
playground.onkey(key="Left", fun=gorg.left)
playground.onkey(key="Right", fun=gorg.right)

while (True):
    gorg.move()
    time.sleep(0.05)
    playground.update()
    
    # detect collision with food
    if (gorg.snake_head.distance(akly) < 15):
        board.score += 1
        board.display()
        akly.gotoRandPos()
playground.exitonclick()
