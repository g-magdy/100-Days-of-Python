from turtle import Screen # we only need a screen not a turtle
from Paddle import Paddle
from Ball import Ball
from scoreboard import ScoreBoard
import time
screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The famous Pong Game!")

p1 = Paddle((370, 0))
p2 = Paddle((-370, 0))
ball = Ball()
board = ScoreBoard()

screen.listen()
screen.onkeypress(fun=p1.up, key="Up")
screen.onkeypress(fun=p1.down, key="Down")
screen.onkeypress(fun=p2.up, key="w")
screen.onkeypress(fun=p2.down, key="s")


game_is_on = True
board.displayScore()
while game_is_on:
    time.sleep(ball.move_speed)
    ball.moveupright()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if p1.touch(ball):
        print("right player")
    if p2.touch(ball):
        print("left player")
    if ball.xcor() > 400:
        print("left player scores 1")
        board.leftScores()
        ball.reset_position()
    if ball.xcor() < -400:
        print("right player scores 1")
        board.rightSores()
        ball.reset_position()
    if (board.l_score >= 10 or board.r_score >= 10):
        game_is_on = False
    board.displayScore()
    screen.update()

screen.exitonclick()
