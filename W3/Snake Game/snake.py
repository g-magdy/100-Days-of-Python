from turtle import Turtle
STRTING_CELLS = 9
STEP = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self) -> None: # the constructor of the class snake
        # every statement here will get executed when creating a snake object
        self.snake_cells = [] # this is a call (an execution)
        self.create_snake() # this is a call (an execution)
        self.head = self.snake_cells[0]
        
    def create_snake(self): # this is a definition of a method
        for cell in range(STRTING_CELLS): # do not put this in the ctor
            t = Turtle()
            t.color("white")
            t.shape("square")
            t.penup()
            t.setx(-20 * cell)
            self.snake_cells.append(t)
    
    def move(self): # this is a definition of a method
        for index in range(STRTING_CELLS - 1, 0, -1):
            pos = self.snake_cells[index-1].position()
            self.snake_cells[index].goto(pos)
        self.head.fd(STEP)
    
    def go_up(self): # the parentheses after the heading() are important
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def go_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            