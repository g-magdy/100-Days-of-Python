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
        for cell in self.cells:
            cell.fd(STEP_SIZE)
        '''
        self.head.forward(STEP_SIZE) # don't forget to advance the head
        # don't forget to start from len() - 1
        # don't forget to add the step (-1) : decrement
        for i in range(len(self.cells) - 1, 0, -1):
            pos = self.cells[i-1].position() # don't forget the brackets here!!
            self.cells[i].goto(pos)
    
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