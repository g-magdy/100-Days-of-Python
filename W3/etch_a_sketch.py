import turtle
tim = turtle.Turtle()
sketch = turtle.Screen()

tim.color("White")
sketch.bgcolor("#191919")

def advance():
    tim.fd(10)

def retard():
    tim.backward(10)

def cw():
    tim.right(10)

def ccw():
    tim.left(10)
    
def empty_sketch():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

sketch.listen()

sketch.onkey(fun=advance, key='w')
sketch.onkey(fun=retard, key='s')
sketch.onkey(fun=cw, key='d')
sketch.onkey(fun=ccw, key='a')
sketch.onkey(key='c', fun=empty_sketch)

sketch.exitonclick()