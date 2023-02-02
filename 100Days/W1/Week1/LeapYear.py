'''
A leap year is a trick to avoid seasons shift : it contains 366 days (29th of february)
It is a leap year
if a year is divisible by 4
    if it is not divisible by 100
    unless it is divisible by 400
'''
year = int(input("Which year do you want to check? "))
if year % 4 == 0: # divisible by 4
    if year % 100 != 0: # not divisible by 100
        print("Leap year.")
    else:
        if year % 400 == 0: # divisible by 400
            print("Leap year.")
        else:
            print("Not leap year.")
else:
    print("Not leap year")