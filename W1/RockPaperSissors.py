from RPS_art import rock, paper, scissors, RPS
import random
import os
os.system("cls")
print("welcome to rock paper scissors 😀")
print(RPS)

decision = 0
while decision != -1:
    decision = int(input("What do you choose, Rock(0)- paper(1) - sissors(2), type -1 to exit\n"))
    os.system("cls")
    choices = [rock, paper, scissors]
    if decision == -1:
        print("GoodBye 👋")
    elif decision >= 3:
        print('Invalid choice')
    else:
        print("Your choice : \n"+choices[decision])
        computerPlay = random.randint(0, 2)

        print("Computer's Choice : \n"+choices[computerPlay])

        if decision >3:
            print("You chose an invalid number, you lose 🙃")
        elif computerPlay == 0:
            if decision == 0:
                print("tie")
            elif decision == 1:
                print("You win 😄")
            else:
                print("You lose 🙃")
        elif computerPlay == 1: #paper
            if decision == 0:
                print("You lose 🙃")
            elif decision == 1:
                print("It is a tie")
            else:
                print("You win 😄")
        else:
            if decision == 0:
                print("You win 😄")
            elif decision == 1:
                print("You lose 🙃")
            else:
                print("It is a tie")
