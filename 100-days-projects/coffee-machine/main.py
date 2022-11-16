# Importing files
from menu_data import resources
from menu_data import MENU
from art import logo

# List of all the interface commands
machine_commands = ['espresso', 'latte', 'cappuccino', 'report', 'off', 'refill']


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino): Done
# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt. Done
# TODO: 3. Print report. Done
# TODO: 4. Check resources sufficient? Done
# TODO: 4 check my light theme please


def user_coffee():
    """Main code for coffee machine"""
    user_choice = input('\nWhat would you like?\nCoffee: ').lower()

    # While loop to check if the user has entered a valid input
    while user_choice not in machine_commands:
        print('Sorry we do not supply that coffee')
        print('\nAvailable coffees: Espresso, Latte and Cappuccino')
        user_choice = input('\nWhat would you like?\nCoffee: ').lower()

    # Checking if the machine has enough resources for the users drink choice
    if user_choice == 'espresso':
        if MENU['espresso']['ingredients']['water'] <= resources['water']:
            if MENU['espresso']['ingredients']['coffee'] <= resources['coffee']:

                # If so continue to payment function
                pay(user_choice)
                # Then start the coffee machine interface again for the next customer
                user_coffee()

            # If the machine does not have the resources print what it is missing
            else:
                print('Sorry the machine does not have sufficient coffee')
                user_coffee()

        else:
            print('Sorry the machine does not have sufficient water')
            user_coffee()

    # Repeating the previous if statement with different drinks
    elif user_choice == 'latte' or user_choice == 'cappuccino':
        if MENU[user_choice]['ingredients']['water'] <= resources['water']:
            if MENU[user_choice]['ingredients']['milk'] <= resources['milk']:
                if MENU[user_choice]['ingredients']['coffee'] <= resources['coffee']:

                    pay(user_choice)
                    user_coffee()

                else:
                    print('Sorry the machine does not have sufficient coffee')
                    user_coffee()

            else:
                print('Sorry the machine does not have sufficient milk')
                user_coffee()

        else:
            print('Sorry the machine does not have sufficient water')
            user_coffee()

    # Adding a command to print out what resources the machine has
    elif user_choice == 'report':
        print(format_resources())
        user_coffee()

    # Adding a command to shut the machine off
    elif user_choice == 'off':
        input('Enter administration password: ')
        print('Machine shutting down...')
        exit()

    # Adding a command to call the function refill
    elif user_choice == 'refill':
        refill()
        user_coffee()


def refill():
    """Asks the user how much water, milk and coffee they would like to refill the machine with and updates the
    dict resources with the values they enter"""
    print('\nEntered refilling machine mode')
    water = int(input('How much water in miller litres what you like to refill?\nWater: '))
    resources['water'] += water

    milk = int(input('How much milk in miller litres what you like to refill?\nMilk: '))
    resources['milk'] += milk

    coffee = int(input('How much coffee in grams what you like to refill?\nCoffee: '))
    resources['coffee'] += coffee

    print('Refilled! \nRestarting machine...')


def consume(user_choice):
    """Updates the dict resources when a user successfully makes a coffee"""
    if user_choice == 'espresso':
        resources['water'] -= MENU[user_choice]['ingredients']['water']
        resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
    else:
        resources['water'] -= MENU[user_choice]['ingredients']['water']
        resources['milk'] -= MENU[user_choice]['ingredients']['milk']
        resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']


# TODO: 5. Process coins.
# TODO: 6. Check transaction successful?

def pay(user_choice):
    """Asks the user how many of each coin they would like to insert into the machine and checks if they entered
    enough for the desired coffee"""

    user_amount = 0.0

    print('\nPlease insert coins')

    pounds = int(input('How many pounds?: '))
    user_amount += pounds

    fifty = int(input('How many 50p pieces?: '))
    user_amount += (fifty * 0.5)

    twenty = int(input('How many 20p pieces?: '))
    user_amount += (twenty * 0.2)

    ten = int(input('How many 10p pieces?: '))
    user_amount += (ten * 0.1)

    five = int(input('How many 5p pieces?: '))
    user_amount += (five * 0.05)

    two = int(input('How many 2p pieces?: '))
    user_amount += (two * 0.02)

    one = int(input('How many 1p pieces?: '))
    user_amount += (one * 0.01)

    if user_amount == MENU[user_choice]['cost']:
        resources['money'] += MENU[user_choice]['cost']
        print(f'Here is your {user_choice.title()}. Enjoy!”')
        print(user_choice)
        consume(user_choice)

    elif user_amount > MENU[user_choice]['cost']:
        resources['money'] += MENU[user_choice]['cost']
        change = user_amount - MENU[user_choice]['cost']
        print(f'\nYou received £{round(change, 2)} in change')
        print(f'\nHere is your {user_choice.title()}. Enjoy!”')
        consume(user_choice)

    else:
        print('Sorry that\'s not enough money. Money refunded.')


def format_resources():
    """Formats the dict resources into a more readable string and returns it"""
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = resources['money']
    return f'\nThe machine now holds:\nWater: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: £{money}'


# TODO: 7. Make Coffee
def coffee_machine():
    """Runs the coffee machine"""
    print(logo)
    user_coffee()


# Starting the coffee machine by calling coffee_machine
coffee_machine()
