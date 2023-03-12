import turtle
import time # IMPORTANT
from snake import Snake
from food import Food
from scoreboard import Scoreboard
playground = turtle.Screen()
LIMIT = 600
playground.setup(width=LIMIT, height=LIMIT)
playground.bgcolor("Black")
playground.title("My Snake Game")
playground.tracer(0)

gorg = Snake()
akly = Food()
board = Scoreboard()

playground.listen()
playground.onkey(key="Up", fun= gorg.up) # type the name without the ()
playground.onkey(key="Down", fun=gorg.down)
playground.onkey(key="Left", fun=gorg.left)
playground.onkey(key="Right", fun=gorg.right)

def hitWall() -> bool:
    if (abs(gorg.snake_head.xcor()) > 280):
        return True
    elif (abs(gorg.snake_head.ycor()) > 280):
        return True
    else:
        return False

def hitTail() ->bool:
    for segment in gorg.snake_segments[1:]: # Slicing the head ()
        # if (segment == gorg.snake_head):
        #     continue # this word almost saved my life
        if (gorg.snake_head.distance(segment) < 10):
            return True
    
    return False
        
game_is_on = True
while (game_is_on):
    gorg.move()
    time.sleep(0.05)
    playground.update()
    
    # detect collision with food
    if (gorg.snake_head.distance(akly) < 15):
        board.score += 1
        gorg.grow()
        board.display()
        akly.gotoRandPos()
    
    # detect collision 
    if (hitWall() or hitTail()):
        board.gameOver()
        game_is_on = False    

playground.exitonclick()
