# Importing modules
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    print('\n' * 10)
    print('Coffee Machine\n')
    choice = input(f'What would you like? ({options}): ').lower()

    if choice == 'off':
        is_on = False
        print('\nShutting down...')
        break

    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
        continue
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
