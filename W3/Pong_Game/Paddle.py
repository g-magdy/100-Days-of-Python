from turtle import Turtle
# inheritance form the turtle class
class Paddle(Turtle):
    def __init__(self, location) -> None:
        super().__init__() # A very important line
        self.shape("square")
        self.color("white")
        self.penup()
        self.setheading(90)
        self.setpos(location)
        self.turtlesize(stretch_len=5.0, stretch_wid=1.0)        
        
    def up(self):
        if (self.ycor() < 240):
            self.forward(20)
        
    def down(self):
        if (self.ycor() > -240):
            self.backward(20)
        
    def touch(self, ball):
        if (self.distance(ball) < 55 and self.distance(ball) > 20) and (ball.xcor() > 340 or ball.xcor() < -340):
            ball.bounce_x()
            return True
        
        return False
