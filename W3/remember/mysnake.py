import turtle
import time # IMPORTANT
from snake import Snake
playground = turtle.Screen()
playground.setup(width=700, height=700)
playground.bgcolor("black")
playground.title("My Snake Game")
playground.tracer(0)

gorg = Snake()
playground.update()

playground.listen()
playground.onkey(key="Up", fun= gorg.up) # type the name of the function without the ()
playground.onkey(key="Down", fun=gorg.down)
playground.onkey(key="Left", fun=gorg.left)
playground.onkey(key="Right", fun=gorg.right)

while (True):
    gorg.move()
    time.sleep(0.05)
    playground.update()
    
playground.exitonclick()
