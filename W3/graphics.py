from turtle import Turtle, Screen
import heroes
import random
# you might have to install a module from 
# import modulename
# from modulename import x, y, z
# from modulename import * # this is not a good practice
# import modulenameeeeee_efjn_buab_igi as name # simpler naming
myscreen = Screen()
myscreen.bgcolor("#191919")
myscreen.colormode(255) # to make the turtle.color() accept values from 0 to 255
samira = Turtle()
#hanafy = Turtle()
samira.shape('turtle')
samira.color("#02b3e4") # udacity's blue

def randomRGB_tuple():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def draw_square(myturtle):
    for _ in range(4):
        myturtle.fd(200)
        myturtle.left(90)

def draw_euilateral_triangle(myturtle):
    for _ in range(3):
        myturtle.fd(200)
        myturtle.right(120)

def draw_hexagon(myturtle):
    for _ in range(6):
        myturtle.fd(200)
        myturtle.right(60)

def draw_regular_polygon(myturtle, n_sides, direction):
    theta = 360 / n_sides
    for _ in range(n_sides):
        myturtle.fd(100)
        if direction == 'up':
            myturtle.left(theta)
        else:
            myturtle.right(theta)

def draw_dashed_lines(myturtle, num_dashes):
    for _ in range(num_dashes):
        myturtle.fd(10)
        myturtle.penup()
        myturtle.fd(10)
        myturtle.pendown()
    
mycolors = ['lime', 'blue', 'red', 'orange', 'white', 'green', 'yellow', 'chartreuse', 'aquamarine']
def draw_strange_flower():
    for n in range(3, 11):
        r = random.randint(0, len(mycolors)-1)
        samira.color(mycolors[r])
        draw_regular_polygon(samira, n, 'up')


def random_walk(myturtle, n): 
       
    myturtle.hideturtle()
    myturtle.pensize(10)
    myturtle.speed(15)
    angles = [0, 90, 180, 270]
    for _ in range(n):
        angle =  random.choice(angles)
        clr = randomRGB_tuple()
        myturtle.color(clr)
        myturtle.fd(40)
        myturtle.setheading(angle)
        
#hanafy.color('White')
# samira.fd(123)
# samira.right(120)
random_walk(samira, 200)
#draw_square(samira)
#draw_hexagon(samira)
#samira.pendown()
#draw_dashed_lines(samira, 10)


#print(heroes.gen())

# draw_regular_polygon(hanafy, n, 'down')













myscreen.exitonclick()