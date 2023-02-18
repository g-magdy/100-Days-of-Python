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
for i in range(6):
    t= Turtle()
    t.color('white')
    t.shape('square')
    t.penup() # before making any move , even setting position 
    t.setposition(-20*i,0) # turtles are 20*20px
    snake_cells.append(t)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    playground.update() # after the whole snake has moved
    
    for cell in range(len(snake_cells) - 1, 0, -1):
        pos = snake_cells[cell-1].position()
        snake_cells[cell].goto(pos)
    snake_cells[0].fd(10)















playground.exitonclick()