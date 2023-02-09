import os
def PerformCalculation(a, operator, b):
    if operator == '+':
        return float(a + b)
    elif operator == '-':
        return float(a - b)
    elif operator == '*':
        return float(a * b)
    elif operator == '/':
        return float(a / b)
os.system('cls')
begin = 'n'
while begin == 'n':
    first_number = float(input("What is the first number ? "))
    print("+\n-\n*\n/\n")
    
    move_on = 'y'
    while move_on == 'y':
        operation = input("Pick an operation : ")
        second_number = float(input("What is the second number ? "))
        result = PerformCalculation(first_number, operation, second_number)
        if result != None:
            print(f"{first_number} {operation} {second_number} = {result}")
        else:
            print("Invalid operation :(\nCalculator stopped")
            begin = False
            break
            
        move_on = input(f"type 'y' to continue calculating with {result}\nType 'n' to start a new calculation\nType 'e' to exit the calculator\n")
        if move_on == 'y':
            first_number = result
        elif move_on == 'n':
            break
        elif move_on == 'e':
            print("Good bye👋")
            move_on = 'stop'
        else:
            print("Unsupported :(")
            break
        
    

# what is the first number ?
# pick an operation
# what is the second number ?
# display operation steps
    # type y or n
    # y >> first number = result
    # n >> restart