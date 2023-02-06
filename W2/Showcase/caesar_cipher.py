import os
from caesar_data import logo, alphabet, caesar
os.system("cls")
print("Welcome to caesar cipher")
print(logo)
request = "yes"
while request == "yes":
    message = input("Type your message below\n").lower()
    shift = int(input("Type the shift number\n"))
    mode = input("Choose a mode : encode / decode\n")
    caesar(message, shift, mode)
    request = input("Go again ? (yes/no) ")
    if request == "no":
        print("Thank you\nGood bye 👋")