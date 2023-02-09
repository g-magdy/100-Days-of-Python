import os
from Art_of_w2 import Calculator_logo
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

def Is_valid(c):
    return c == '+' or c == '-' or c == '*' or c == '/'

calc = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}

# i can add more functions to this thing

def Calculate():
    os.system("cls")
    print(Calculator_logo)
    num1 = float(input("what is the first number ? "))
    should_continue = True
    while should_continue:
        print("Operations : ")
        for key in calc:
            print(key)
        operation = input("which operation ? ")
        if not Is_valid(operation):
            print("Not a valid operation :(")
            break
        function = calc[operation]
        num2 = float(input("what is the second number ? "))
        result = function(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        choice = input(f"type 'y' to continue calculating with {result}\nType 'n' to start a new calculation\nType 'e' to exit the calculator\n")
        if choice == 'y':
            num1 = result
        elif choice == 'n':
            Calculate()
        elif choice == 'e':
            print("Good bye 👋")
            should_continue = False
        else:
            print("Invalid choice :(")
            should_continue = False

Calculate()