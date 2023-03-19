from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_step = 10
        self.y_step = 10
        self.move_speed = 0.05
    def moveupright(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)
    
    def reset_position(self):
        self.x_step = self.x_step * -1
        self.move_speed = 0.05
        self.goto(0, 0)
        
    def bounce_y(self):
        self.y_step = self.y_step * -1
    
    def bounce_x(self):
        self.move_speed *= 0.9
        self.x_step = self.x_step * -1