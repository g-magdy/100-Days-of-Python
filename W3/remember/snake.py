from turtle import Turtle
STARTING_CELLS = 6
STEP_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create()
        self.snake_head = self.snake_segments[0]

    def create(self):
        for i in range (STARTING_CELLS):
            t = Turtle(shape="square")
            t.color("white")
            t.penup()
            t.setx(-20*i)
            self.snake_segments.append(t)
        
    # the best part is how to make the body follow the head
    # that is the wrong way to think about it
    # make it a push from behind not a pull

    def move(self):
        for segment in range(len(self.snake_segments)-1, 0, -1):
            front_of_me_pos = self.snake_segments[segment - 1].position()
            self.snake_segments[segment].goto(front_of_me_pos)
        self.snake_segments[0].fd(STEP_SIZE)
    
    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
        
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
        
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
        
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)