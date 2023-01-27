treasure = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''
print("Welcome to treasure Island")
print("Your mission is to find the treasure - please maximize your terminal")
print("You are at a cross road.")
a = input('where do you want to go ? type "left" or "right"\n').lower()
if a == "left":
    print("You come to a lake. There is an island in the middle of the lake.")
    b = input('Type "wait" to wait for a boat, or type "swim" to swim across\n').lower()
    if b == "wait":
        print("You arrive at the Island Unharmed, There are 3 doors. one red, one yellow, and one blue")
        c = input("which one do you choose ?\n").lower()
        if c == "yellow":
            print(treasure)
            print("You found the treasure")
        elif c == "red":
            print("you are on fire bro")
        elif c == "blue":
            print("Blue beasts are eating me")
        else:
            print("This door does not exit. game over.")
    else:
        print("Wait is this a shark?! AAAA..")
else:
    print("You fell into a black hole. Game over")