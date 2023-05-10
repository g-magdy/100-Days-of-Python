import time
from turtle import Screen
from player import Player
from carManager import CarManager
from scoreBoard import ScoreBoard
import info_and_prams as const
    

playground = Screen()
playground.bgcolor(const.BG_COLOR)
playground.setup(width=const.SCREEN_SIDE, height=const.SCREEN_SIDE)
playground.title("Cross the road if you can | press 's' to stop the cars then exit")
playground.tracer(0)
tut = Player()
cars = CarManager()
judge = ScoreBoard()

game_is_on = True
rate = const.SCREEN_SLEEP
def leave():
    global game_is_on
    game_is_on = False

playground.listen()
playground.onkey(fun=leave, key="s")
playground.onkeypress(fun=tut.moveUp, key="Up") # it is allowed to keep the key down and move


while (game_is_on):
    time.sleep(rate)
    playground.update()
    judge.showLevel()
    cars.advance()
    if cars.collide(tut):
        judge.gameOver()
        break
    if (tut.passedFinishLine()):
        judge.levelUp()
        rate /= 1.4
        tut.resetPos()

playground.exitonclick()