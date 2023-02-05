def ShowDict(Dict):
    for key in Dict:
        print(f"{key} : {Dict[key]}")
another_auction = "yes"
while another_auction == "yes":
    Auction = {}   
    more_people = "yes"
    print("Auction Started")
    while more_people == "yes":
        person = input("What is your name sir ?\n")
        bid = float(input("What is your bid?\n$"))
        Auction[person] = bid
        more_people = input("Are there more people? (yes/no)\n")
    ShowDict(Auction)
    another_auction = input("Do you want another auction? (yes/no)\n")
print("Thank you 😊")