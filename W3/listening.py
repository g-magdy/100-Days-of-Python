import turtle

tim = turtle.Turtle()
canvas = turtle.Screen()

def moveForawd():
    tim.forward(100)

# need to bind a function to a key
canvas.listen()
canvas.onkey(fun=moveForawd, key='Right')

canvas.exitonclick()