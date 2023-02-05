Auction = {}
again = "yes"
while again != "no":
    person = input("What is your name sir ?\n")
    bid = float(input("What is your bid?\n$"))
    Auction[person] = bid
    again = input("Are there more people? (yes/no)\n")
print(Auction)