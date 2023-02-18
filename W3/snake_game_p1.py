'''
1 create snake's body OK
2 continuously move the snake
3 control its movement
4 put food on random position 
5 detect collision with food
    grow snake
    put another food in random location
6 score automatically updates
7 end game :
    detect collision with wall
    detect collision with tail
'''
from turtle import Screen, Turtle
import time
playground = Screen()
playground.tracer(0) #IMPORTANT - The screen will preserve its state until you manually call update
playground.bgcolor('black')
playground.setup(width = 600, height= 600)
playground.title("Welcome to the snake game!")
snake_cells = []
for i in range(3):
    t= Turtle()
    t.color('white')
    t.shape('square')
    t.penup() # before making any move , even setting position 
    t.setposition(-20*i,0) # turtles are 20*20px
    snake_cells.append(t)

for l in range(30):
    for i in range(3):
        snake_cells[i].fd(10)
        time.sleep(0.01)
    playground.update() # after the whole snake has moved
playground.exitonclick()