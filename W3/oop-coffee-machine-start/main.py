from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

our_machine = CoffeeMaker()
cashier = MoneyMachine()
drinks_menu = Menu()
machine_is_on = True
while machine_is_on:    
    request = input(f"What would you like {drinks_menu.get_items()} ? ")
    if request == 'off':
        machine_is_on = False
    elif request == 'report':
        our_machine.report()
        cashier.report()
    else:            
        customer_drink = drinks_menu.find_drink(request)
        if customer_drink != None:
            if our_machine.is_resource_sufficient(customer_drink):
                if cashier.make_payment(customer_drink.cost):
                    our_machine.make_coffee(customer_drink)
    
print("Good Bye 👋")