import turtle
import random


turtle.colormode(255)

blue_palette = ["#0779E4", "#4CBBB9", "#77D8D8", "#EFF3C6"]

def choose_random_rgb_tuple():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
    
def draw_sipro_circles(my_turtle, gap):
    for _ in range(int(360 / gap)):
        #my_turtle.color(choose_random_rgb_tuple()) # version 1
        #my_turtle.color("#02b3e4") # vesion 2
        my_turtle.color(random.choice(blue_palette)) # version 3
        my_turtle.circle(150)
        my_turtle.left(gap)


tim = turtle.Turtle()
tim.hideturtle()
tim.pencolor("white")
tim.speed(0)

#tim.pensize(10)

canvas = turtle.Screen()
canvas.bgcolor("#191919")

draw_sipro_circles(tim, 6)

canvas.exitonclick()