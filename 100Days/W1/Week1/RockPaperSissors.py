import random
decision = int(input("What do you choose, Rock(0)- paper(1) - sissors(2)\n"))
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = ''' 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choices = [rock, paper, scissors]

if decision >= 3:
    print('Invalid choice')
else:
    print("Your choice : \n"+choices[decision])
    computerPlay = random.randint(0, 2)

    print("Computer's Choice : \n"+choices[computerPlay])

    if decision >3:
        print("You chose an invalid number, you lose")
    elif computerPlay == 0:
        if decision == 0:
            print("tie")
        elif decision == 1:
            print("You Win")
        else:
            print("You lose")
    elif computerPlay == 1: #paper
        if decision == 0:
            print("You lose")
        elif decision == 1:
            print("tie")
        else:
            print("You win")
    else:
        if decision == 0:
            print("You win")
        elif decision == 1:
            print("You Lose")
        else:
            print("It is a tie")
