# Importing files
import art


def add(n1, n2):
    """Adds two numbers together"""
    return n1 + n2


def subtract(n1, n2):
    """Subtracts number 2 (n2) from number 1 (n1)"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplies two numbers"""
    return n1 * n2


def divide(n1, n2):
    """Divides number 1 (n1) by number 2 (n2)"""
    return n1 / n2


# printing title art
print(art.logo)


def calculation():
    """Asks the user what they would like to calculate, and prints the answers"""
    # Assigning calculation_finished to True
    calculation_finished = False

    # Dict that holds symbols as keys and functions as values
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

    # Asking the user for the first number
    num1 = float(input('Enter the first number below \nNumber 1: '))
    # Printing a new line
    print('\n')

    # Printing all the symbols (keys) in dict operations
    for operator in operations:
        print(operator)
    # Printing new line
    print('\n')

    # Asking the user to enter a symbol/operator to use with their numbers
    operation_symbol = input('Enter an operator from above ^ \nOperator: ')
    # Asking the user for the second number
    num2 = float(input('\nEnter the second number below \nNumber 2: '))

    # Assigning the value function to calculation_function
    calculation_function = operations[operation_symbol]

    # Assigning first_answer the function calculation_function with two arguments
    first_answer = calculation_function(num1, num2)

    # Printing the calculation with the answer
    print(f'\n{num1} {operation_symbol} {num2} = {first_answer}')

    # Assigning the old_answer to first_answer
    old_answer = first_answer

    # While loop to check if the user has finished calculating
    while not calculation_finished:
        # Asking the user if they have finished calculating
        finish = input(f'\nAre you finished with {old_answer}\n(Y/N):  ').lower()
        # If the user entered 'y' then the function calculation() will ru again (recursion)
        if finish == 'y':
            # Stopping the while loop
            calculation_finished = True
            print('\nClearing result...\n')
            calculation()

        # Asking the user to enter a symbol/operator to use with their numbers
        operation_symbol = input('\nEnter an operator \nOperator: ')
        # Asking the user for the new number
        new_num = float(input('\nEnter a new number \nNew number: '))
        # Assigning the value function to calculation_function
        calculation_function = operations[operation_symbol]
        # Assigning new_answer the function calculation_function with two arguments
        new_answer = calculation_function(old_answer, new_num)

        # Printing the calculation with the answer
        print(f'\n{old_answer} {operation_symbol} {new_num} = {new_answer}')

        # Assigning new_answer to old_answer
        old_answer = new_answer


# Calling calculation()
calculation()
