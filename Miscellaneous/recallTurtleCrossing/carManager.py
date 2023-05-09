import random
from turtle import Turtle, colormode
import info_and_prams as const

class CarManager:
    def __init__(self):
        self.cars = []
        for _ in range(const.NUM_CARS):
            self.addCar()
        
    def addCar(self):
        t = Turtle(shape="square")
        t.penup()
        t.speed(0)
        t.seth(180)
        t.shapesize(stretch_len=2.0, stretch_wid=1.0)
        colormode(255)
        #randClr = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        randClr = random.choice(const.colors)
        randX = random.randint(-const.SCREEN_SIDE//2 + 20,  const.SCREEN_SIDE//2 -20)
        randY = random.randint(-const.SCREEN_SIDE//2 + 40,  const.SCREEN_SIDE//2 -10)
        t.color(randClr)
        t.goto(randX, randY)
        self.cars.append(t)
    
    def advance(self):
        for car in self.cars:
            if car.xcor() < -const.SCREEN_SIDE//2 :
                car.setx(const.SCREEN_SIDE//2)
            else:
                car.fd(const.CARS_STEP_SIZE)
    
    def collide(self, player):
        for car in self.cars:
            if (car.distance(player) < 20):
                return True
        return False