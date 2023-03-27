from turtle import Turtle
import random
colors = ["red", "orange", "yellow", "green", "blue", "purple", "white", "cyan"]
'''        self.shapesize(stretch_wid=2, stretch_len= 1)
        self.shape("square")
'''
INIT_STEP_SIZE = 10
class CarManager:
    def __init__(self) -> None:
        self.all_cars = []
        self.move_speed = INIT_STEP_SIZE
        pass   
    
    def throwCar(self):
        if (random.randint(1, 5) == 1):
            t = Turtle("square")    
            t.color(random.choice(colors))
            t.penup()
            t.setheading(180)
            t.shapesize(stretch_len=2.0)
            t.setx(300)
            t.sety(random.randint(-250, 250))
            self.all_cars.append(t)
    
    def moveCars(self):
        for car in self.all_cars:
            if (car.xcor() < -270):
                car.setx(300)
            
            car.forward(self.move_speed)
    
    def detectCollision(self, player):
        for car in self.all_cars:
            if player.distance(car) < 25:
                return True
    
    def increaseSpeed(self):
        self.move_speed *= 1.1