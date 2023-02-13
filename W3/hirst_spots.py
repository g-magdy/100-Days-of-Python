#import colorgram
# raw = colorgram.extract('hirst_colors.jpg', 10)

# rgb_hirst_palette = []
# for color in raw:
#     rgb_color = color.rgb    # extract rgb
#     pure = (rgb_color.r, rgb_color.g, rgb_color.b) # put each ingredient in its place 
#     rgb_hirst_palette.append(pure)

# print(rgb_hirst_palette)

import random, turtle
turtle.colormode(255)
tim = turtle.Turtle()
tim.penup()
tim.color("white")
canvas = turtle.Screen()
canvas.bgcolor("#000000")
palette = [(234, 166, 59), (44, 113, 157), (112, 151, 203), (212, 123, 164), (16, 129, 96), (152, 19, 56), (1, 177, 144)]

def draw_hist(my_turtle, l, w):
    my_turtle.speed(0)
    my_turtle.penup()
    my_turtle.goto(-225, -225)
    for row in range(1, 1+w):        
        for _ in range(l):
            my_turtle.dot(20, random.choice(palette))
            my_turtle.fd(50)
        my_turtle.goto(-225, -225 + row*50)
    my_turtle.hideturtle()

draw_hist(tim, 10, 10)


canvas.exitonclick()