print("Welcome to the tip calculator 😀")
Cost = float(input("What was the total bill? $"))
n = int(input("how many people to split the bill? "))
percent_tip = float(input("What percentage tip would you like to give ? %"))/100
total = Cost+Cost*percent_tip # calculate percentage tip
splitCost = round(total / n, 2)
final_amount = "{:.2f}".format(splitCost)
print(f"Every one of the {n} should pay {final_amount}")