from turtle import Screen
import time
REFRESH_RATE = 0.02
scr = Screen()
scr.title("The famous snake game!")
scr.setup(width=600, height=600)
scr.bgcolor("Black")
scr.tracer(0)

from snake import Snake
mysnake = Snake()

game_is_on = True

while game_is_on:
    time.sleep(REFRESH_RATE)
    scr.update()
    scr.onkey(key='w', fun=mysnake.go_up)
    scr.onkey(key='s', fun=mysnake.go_down)
    scr.onkey(key='a', fun=mysnake.go_left)
    scr.onkey(key='d', fun=mysnake.go_right)
    scr.listen()
    mysnake.move()





















scr.exitonclick()