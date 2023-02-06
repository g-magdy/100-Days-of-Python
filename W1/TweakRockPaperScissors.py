import os
from RPS_art import rock, paper, scissors, RPS
Choices = [rock, paper, scissors]
os.system("cls")
print("Welcome to rock Pper scissors - لو دكر اكسبني")
print(RPS)
userChoice = 0
while userChoice != -1:
    userChoice = int(input("Choose : Rock (0) | Paper (1) | Scissors (2).\nType -1 to give up\n"))
    os.system("cls")
    MachineChoice = -1
    if userChoice == -1:
        print("سلام يابن العبيطة 😂")
        break
    elif userChoice >= 3:
        print("Invalid choice")
        continue
    elif userChoice == 0:
        MachineChoice = 1
    elif userChoice == 1:
        MachineChoice = 2
    else:
        MachineChoice = 0
    print("Your choice: \n")
    print(Choices[userChoice])
    print("Computer choice: \n")
    print(Choices[MachineChoice])
    print("You Lose 😆")