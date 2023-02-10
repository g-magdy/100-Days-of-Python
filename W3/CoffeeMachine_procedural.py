import os
drinks = [
    {
        'name': 'espresso',
        'price': 1.5,
        'water': 50,
        'coffee': 18,
        'milk': 0
    },
    {
        'name': 'latte',
        'price': 2.5,
        'water': 200,
        'coffee': 24,
        'milk': 150
    },
    {
        'name': 'cappuccino',
        'price': 3,
        'water': 250,
        'coffee': 24,
        'milk': 100
    }
]


water_tank = 300
milk_tank = 200
coffee_tank = 100
our_money = 0


def print_report():
    '''prints the values of current resources'''
    print(f"Water: {water_tank}ml")
    print(f"Milk: {milk_tank}ml")
    print(f"Coffee: {coffee_tank}g")
    print(f"Money: ${our_money}")
    

def sufficient_resources_for(drink)-> bool: 
    '''takes a dink and returns true if the avalable resources can affors to make it'''
    return water_tank >= drink['water'] and milk_tank >= drink['milk'] and coffee_tank >= drink['coffee']


def calc_value(quarters, dimes, nickles, pennies):
    return quarters*0.25 + dimes * 0.01 + nickles * 0.05 + pennies * 0.01


def process_transaction(paid_amount, requested):
    '''Takes an amount of money and a drink {dictionary}
        then decides if the money is sufficient to make this drink
        updates the machine resources
    '''
    if paid_amount < requested['price']:
        print("Insufficient money")
        return False
    
    global water_tank, coffee_tank, milk_tank
    water_tank -= drink['water']
    coffee_tank -= drink['coffee']
    milk_tank -= drink['milk']
    return True
    
    
def in_menu(order):
    for drink in drinks:
        if drink['name'] == order:
            return drink # this is trueee - but i need a return value of type dictionary 
    return False # if you did not find a drink with this name
    
#####################################
os.system("cls")
end_of_visit = False

while not end_of_visit:
    request = input("  What would you like ? (espresso/latte/cuppoccino) : ")
    
    if request == 'report':
        print_report()
        continue
    elif request == 'leave':
        print("Good bye 👋")
        end_of_visit = True
        continue
    
    if not in_menu(request):
        print("I cannot understand your request")
    
    elif not sufficient_resources_for(in_menu(request)):
        print("Insufficient resources in the machine :(")
    else:
        print("Please insert coins")
        quarters = int(input("How many quarters ? "))
        dimes = int(input("How many dimes ? "))
        nickels = int(input("How many nickels ? "))
        pennies = int(input("How many pennies ? "))

        paid_money = calc_value(quarters, dimes, nickels, pennies)
        print(f"paid money is ${round(paid_money, 2)}")
        for drink in drinks:
            if drink['name'] == request:
                if process_transaction(paid_money, drink):
                    our_money += drink['price']
                    change = paid_money - drink['price']
                    print(f"Successful transaction ✅ your change is ${round(change, 2)}")
                    print("Enjoy your drink ☕")
