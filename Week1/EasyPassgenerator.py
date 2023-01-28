import random
alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
symbols = "!@#$%^&*()_<>[]/?"
decimals = "0123456789"
print("Welcome to the Password generator")
l = int(input("Number of letters ?\n"))
s = int(input("How many symbols ?\n"))
n = int(input("How many numbers ?\n"))
# CAN I BUILD one that ranf=domly generates a pasword combination given only the length, yes
# option 0 : randomize for me 
# option 1: I choose the amount of every ingredient
# Let's finish the easy level
password = ""
for i in range (0, l):
    r = random.randint(0, 51) # it spans all
    password += alphabet[r]
for i in range (0, s):
    r = random.randint(0, len(symbols) - 1)
    password += symbols[r]
for i in range (0, n):
    r = random.randint(0, 9)
    password += decimals[r]
print(password)