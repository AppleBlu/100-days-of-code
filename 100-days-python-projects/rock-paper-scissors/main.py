# Importing modules
import random
import time

# Art for rock
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

# Art for paper
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

# Art for scissors
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Assigning random_number a random number
random_number = random.randint(1, 3)

# Printing a welcome message
print('Welcome to Rock Paper Scissors!!!')


# Creating the game
def game():
    """Will start the game"""
    # Allowing the user to pick rock, paper or scissors
    user_choice = input('Enter Rock, Paper or Scissors \nPlay: ').lower()

    # Assigning the users input to 0
    user_choice_in_number = 0

    # Creating an if statement to print the art.py related to users input
    if user_choice == 'rock':
        user_choice_in_number = 1
        print(rock)
    elif user_choice == 'paper':
        user_choice_in_number = 2
        print(paper)
    elif user_choice == 'scissors':
        user_choice_in_number = 3
        print(scissors)

    # Pausing before showing the computers play
    time.sleep(0.5)

    # If statement to print art.py related to the computers play
    if random_number == 1:
        print('Computer picked Rock')
        print(rock)
    elif random_number == 2:
        print('Computer picked Paper')
        print(paper)
    elif random_number == 3:
        print('Computer picked Scissors')
        print(scissors)

    # If statement in the case user and computer had the same play
    if user_choice_in_number == random_number:
        print('You drew with the computer')

    # If statement in the case that users wins
    if user_choice == 'paper' and random_number == 1:
        print('\nYou won!!!')
    elif user_choice == 'scissors' and random_number == 2:
        print('\nYou won!!!')
    elif user_choice == 'rock' and random_number == 3:
        print('\nYou won!!!')

    # If statement in the case that user loses
    if user_choice == 'rock' and random_number == 2:
        print('You lose')
    elif user_choice == 'paper' and random_number == 3:
        print('You lose')
    elif user_choice == 'scissors' and random_number == 1:
        print('You lose')


input('\nPress enter to play\n')
# Running the game 
game()
