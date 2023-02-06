logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
import os
def ShowDict(Dictionary):
    for key in Dictionary:
        print(f"{key} : {Dictionary[key]}")

def ShowWinner(Dictionary):
    max = 0
    winner = ''
    for key in Dictionary:
        if Dictionary[key] > max:
            max = Dictionary[key]
            winner = key
    print(f"Winner is {winner} 🎉")

def Run_Auction():
    Auction = {}   
    more_people = "yes"
    print("Auction Started")
    print(logo)
    while more_people == "yes":
        person = input("What is your name sir ?\n")
        bid = float(input("What is your bid?\n$"))
        Auction[person] = bid
        more_people = input("Are there more people? (yes/no)\n")
        os.system("cls")
    ShowDict(Auction)
    ShowWinner(Auction)
# Start of the main function

another_auction = "yes"
while another_auction == "yes":
    os.system("cls")
    Run_Auction()
    another_auction = input("Do you want another auction? (yes/no)\n")
print("Thank you 😊")