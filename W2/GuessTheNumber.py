import os, random
from Art_of_w2 import Guess_the_number
def Execute_main(number, lives):
    '''play the main game - returns true if the user wins'''
    guess = 0 # initial value
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
            return True
    return False # if he ran out of lives
# START
os.system("cls")
print(Guess_the_number)
print("Welcome to the number guessing game!\nI am thinking of a number between 1 and 100\nCan you guess it ?")
# maybe a little feature can be added to let the user choose the boundaries
number = random.randint(1, 100)
difficulty = input("Choose a dificulty (easy) / (hard): ")
if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5
else:
    lives = 7
if Execute_main(number, lives):
    print("You won the game 🎉")
else:
    print("You ran out of lives")
# END