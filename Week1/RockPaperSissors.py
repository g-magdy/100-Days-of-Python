import random
var = input("What do you choose, Rock(r)- paper(p) - sissors(s)").lower()
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
decision = 0
if var == 'r':
    decision = 0
elif var == 'p':
    decision = 1
elif var == 's':
    decision = 2
else:
    print("invalid choice")

print("Your choice : \n"+choices[decision])

computerPlay = random.randint(0, 2)

print("Computer's Choice : \n"+choices[computerPlay])

if computerPlay == 0:
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
        print("You win")
