# Importing files and modules
from art import logo
import random

# Printing the title logo
print(logo)
print('\n')

# Computer picking a random number form 1 to 100
computers_guess = random.randint(1, 100)


# Class user to hold guesses and update guesses
class User:

    def __init__(self, guesses):
        self.guesses = guesses

    def update_guesses(self, new_guesses):
        self.guesses += new_guesses


# Initializing User with user1 and setting guesses to 0
user1 = User(0)


def set_difficulty():
    """Asks the user to set a difficulty for the game. Options are hard or easy. If easy is entered then they have 10
    guesses else they have 5"""
    # Asking user for the difficulty
    print('What difficulty would you like to select\nEasy\nHard\n')
    difficulty = input('Enter your difficulty: ').lower()

    # While loop to check for invalid inputs
    while difficulty != 'hard' and difficulty != 'easy':
        print('Invalid Input')
        difficulty = input('Enter your difficulty: ').lower()

    # Adds different guess amounts relevant to difficulty
    if difficulty == 'hard':
        user1.update_guesses(5)
    elif difficulty == 'easy':
        user1.update_guesses(10)


def game():
    """Runs the game"""
    # While the user still has guesses left
    while user1.guesses > 0:
        users_guess = int(input('\nGuess: '))

        # Wile they did not enter a correct input
        while users_guess > 100 or users_guess < 1:
            print('Invalid Input')
            users_guess = int(input('Guess a number between 1 and 100 \nGuess: '))

        # Checking if users guess is equal to computers_guess
        if users_guess == computers_guess:
            print(f'\nWow! You guessed it! {computers_guess}')
            exit()
        elif users_guess > computers_guess:
            print('\nNope')
            print('Lower')
            user1.update_guesses(-1)
            game()
        elif users_guess < computers_guess:
            print('\nNope')
            print('Higher')
            user1.update_guesses(-1)
            game()

    print(f'You are out of guesses :(\nThe number was {computers_guess}\nGame Over')
    exit()


# Calling set_difficulty()
set_difficulty()
# Printing how many guesses the user has
print(f'\nYou have {user1.guesses} guesses! Good luck!')
# Asking the user to take a guess at the number
print('\nGuess a number between 1 and 100')
# Calling game()
game()
