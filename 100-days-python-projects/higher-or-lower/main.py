# Importing files and modules
import art
import random
from game_data import data

# Printing the games logo
print(art.logo)

# Assigning rand_index and score to 0
rand_index = 0
score = 0


def get_random_index():
    """Updates rand_index to a random number from 1 to 49"""
    global rand_index
    rand_index = random.randint(1, 49)


def get_data(index):
    """Returns a dict in the list data at the index passed in"""
    return data[index]


def get_data_string(index):
    """Formats the data received by get_data(index) into a readable string and returns it"""
    data_string = ''
    random_data = get_data(index)
    data_string += random_data['name'] + ', '
    data_string += random_data['description'] + ', from '
    data_string += random_data['country']
    return data_string


def get_follower_count(index):
    """Returns the follower count at the index dict of the list"""
    return data[index]['follower_count']


def game(a_account):
    """Runs the game"""
    global score
    a = a_account  # Setting a to the passed in argument
    a_follower_count = get_follower_count(rand_index)
    get_random_index()  # Updating rand_index
    b = get_data_string(rand_index)  # Setting b to a random account formatted
    b_follower_count = get_follower_count(rand_index)
    print(f'Compare A: {a}')
    print(art.vs)  # Printing the vs logo
    print(f'Against B: {b}')
    users_guess = input('\nWho has the most followers? (A/B): ').lower()

    # While loop to check the user entered a valid input
    while users_guess != 'a' and users_guess != 'b':
        print('Invalid Input')
        users_guess = input('\nWho has the most followers? (A/B): ').lower()

    # If statement to check if the user is correct
    if users_guess == 'a' and a_follower_count > b_follower_count:
        print('Correct!\n')
        score += 1  # Increasing score by 1
        game(b)  # Running the game again but setting a to b by passing b as an argument

    # Same again
    elif users_guess == 'b' and a_follower_count < b_follower_count:
        print('Correct!\n')
        score += 1
        game(b)

    # If user is not correct exit code and print score
    else:
        print('Game over')
        print(f'Your score was {score}')
        exit()


# Setting rand_index to a random number and calling game() to play the game
get_random_index()
game(get_data_string(rand_index))
