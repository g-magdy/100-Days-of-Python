from turtle import Turtle

STARTING_CELLS = 7
STEP_SIZE = 10

class Snake:
    def __init__(self) -> None:
        self.cells = []
        self.createSnake()
        self.head = self.cells[0]
    
    def createSnake(self):
        for i in range(STARTING_CELLS):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.setx(-20 * i)
            self.cells.append(t)
            
    def move(self):
        '''
        the idea is simple, advance the head by a step.
        then make each cell follow the one in front of it
        '''
        self.head.forward(STEP_SIZE) # don't forget to advance the head
        # don't forget to start from len() - 1
        # don't forget to add the step (-1) : decrement
        for i in range(len(self.cells) - 1, 0, -1):
            pos = self.cells[i-1].position() # don't forget the brackets here!!
            self.cells[i].goto(pos)
    
    def resetSnake(self):
        #(But does not remove them from the screen do i'll)
        for c in self.cells:
            c.goto(1000, 1000)
        
        self.cells.clear() # delete old snake 
            
        self.createSnake()
        self.head = self.cells[0]
    
    def goRight(self):
        if (self.head.heading() != 180):
            self.head.setheading(0)
    
    def goLeft(self):
        if (self.head.heading() != 0):
            self.head.setheading(180)
        
    def goUp(self):
        if (self.head.heading() != 270):
            self.head.setheading(90)
            
    def goDown(self):
        if (self.head.heading() != 90):
            self.head.setheading(270)
            
    def eatFood(self, food):
        if (self.head.distance(food) < 15):
            food.newPos()
            return True
        else:
            return False
            
    def grow(self):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(self.cells[-1].position())
        self.cells.append(t)
        
    def collision(self):
        # first detect collision with wall
        outX = self.head.xcor() < -295 or self.head.xcor() > 295
        outY = self.head.ycor() < -295 or self.head.ycor() > 295
        if (outX or outY):
            return True
        # second : detect collision with my body
        for segment in self.cells[2:]:
            if (self.head.distance(segment) < 5):
                return True
        
        return False