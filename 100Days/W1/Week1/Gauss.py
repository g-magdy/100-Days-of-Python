a = int(input("lower bound = "))
b = int(input("upper bound = "))
s = 0
for i in range(a, b + 1):
    s += i
print(s)
print("Gauss was amazing!")
'''
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
def pop():
    turn_left()
    h = 0
    while wall_on_right():
        h += 1
        move()
    turn_right()
    move()
    turn_right()
    steps =  h
    while steps > 0:
        steps -= 1
        move()
    turn_left()
while not at_goal():
    if wall_in_front():
        pop()
    elif front_is_clear():
        move()
'''