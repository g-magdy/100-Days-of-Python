print("Welcome to the Roller coaster 😄")
height = float(input("What is your height (cm)? "))
bill = 0
if height < 120:
    print("Sorry you are not allowed here")
else:
    age = int(input("What is you age ? "))
    if age < 12:
        bill += 5
    elif age <= 18:
        bill += 7
    else:
        bill+= 12
    want_photo = input("Do you want a photo ? (Y / N) ")
    if want_photo == 'Y' or want_photo == 'y':
        bill += 3
        
    if age >= 45 and age <= 55: # special user
        bill = 0
    print(f"Welcome to the ride, Your bill is {bill}")