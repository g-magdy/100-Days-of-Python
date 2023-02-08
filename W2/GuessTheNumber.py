import os, random
from Art_of_w2 import Guess_the_number

def Execute_main(number, lives):
    guess = 0 # initial value
    won = False
    while guess != number and lives > 0:
        guess = int(input("What is your guess ? "))
        if guess < number:
            lives -= 1
            print("Too low")
            print(f"Remaining lives = {lives}\n")
        elif guess > number:
            lives -= 1
            print("Too high")
            print(f"Remaining lives = {lives}")
        else:
            won = True
    
    if won:
        print("You won the game 🎉")
        return True
    else:
        print("You ran out of lives")
        return False

###################################
os.system("cls")
print(Guess_the_number)
print("Welcome to the number guessing game!\nI am thinking of a number between 1 and 100\nCan you guess it ?")
# maybe a little feature cn be added to let the user choose the boundaries
number = random.randint(1, 100)
difficulty = input("Choose a dificulty (easy) / (hard): ")
if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5
else:
    lives = 7
won_the_game = Execute_main(number, lives)