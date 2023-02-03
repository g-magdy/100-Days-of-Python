import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Password generator")
l = int(input("Number of letters ?\n"))
s = int(input("How many symbols ?\n"))
n = int(input("How many numbers ?\n"))
# CAN I BUILD one that randomly generates a pasword combination given only the length, yes
# option 0 : randomize for me 
# option 1: I choose the amount of every ingredient
password = []

for i in range(0, l):
    password += random.choice(letters)
for i in range (0, s):
    password += random.choice(symbols)
for i in range (0, n):
    password += random.choice(numbers)
random.shuffle(password)
key = ""
for i in range (0, len(password)):
    key += password[i]
print(key)