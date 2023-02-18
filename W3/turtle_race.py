import turtle
import random
race_track = turtle.Screen()
race_track.title("The Turtle Race")
race_track.bgcolor("#191919")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
num_turtles = len(colors)
race_track.setup(width=500, height=400) # keyword arguments here is preferred
racers = []
for i in range (num_turtles):
    racers.append(turtle.Turtle(shape="turtle"))
    racers[i].penup()
    racers[i].color(colors[i])
    racers[i].goto(x=-230, y= -100 + i*35)

user_bet = race_track.textinput(title="Race is starting! Place your Bet", prompt="Who will win the race ?\nEnter a color : ")

race_is_finished = False
winner = ''
while race_is_finished == False:
    for racer in racers:
        if (racer.xcor() >= 230):
            race_is_finished = True
            winner = racer.fillcolor()
            break
        racer.fd(random.randint(5, 10))
    
turtle.hideturtle()
turtle.pencolor(winner)
turtle.write(f"Winner is  {winner} 🎉\n", align="center",font=('Lemon', 26, 'bold'))
if user_bet == winner:
    turtle.write("You guessed correctly 👏", align='bottom', font=('Lemon', 26, 'bold'))
else:
    turtle.write("Game over", align='center', font=('Lemon', 26, 'bold'))

race_track.exitonclick()