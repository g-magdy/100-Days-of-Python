import time
from turtle import Turtle, Screen

from player import Player
from scoreboard import ScoreBoard
from car_manager import CarManager

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

tut = Player()
board = ScoreBoard()
carManager = CarManager()

game_is_on = True

screen.listen()
screen.onkeypress(fun=tut.moveUp, key="Up")

counter = 1
while game_is_on:
    if counter < 100:
        carManager.throwCar()
    carManager.moveCars()
    board.viewScore()
    time.sleep(0.1)
    if (tut.ycor() > 280):
        tut.restart()
        board.incremetScore()
        carManager.increaseSpeed()
    if (carManager.detectCollision(tut)):
        game_is_on = False
    counter += 1
    screen.update()

board.endgame()
screen.exitonclick()