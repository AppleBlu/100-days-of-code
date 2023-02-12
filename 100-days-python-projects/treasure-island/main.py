# Adding art.py to the application
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

# Printing a welcome message
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print('\n------------------------------------------\n')


# Function to be called when the user dies
def game_over():
    """Game will end and Game Over will be printed"""
    print('Game over\n')
    # Starting the game again
    game()


# Counter for the number of attempts
attempts = 0


# Function to be called to play the game
def game():
    """Will start the game"""
    # Making attempts available in the function
    global attempts
    # Each time game() is called attempts increments by 1
    attempts += 1

    input('Press enter to start')

    # Printing the users attempt
    print(f'\nAttempt {attempts}\n')

    # Printing first question
    print('You have arrived on treasure island! The first thing you encounter is a fork in the road')

    # Printing first question input
    choice = input('Would you like to go left or right? Enter Left or Right \nChoice: ').lower()

    # If else statement for users input on first question
    if choice == 'left':
        print('\nYou come across a lake')
        lake_choice = input('Would you like to wait for a boat or swim across to the other side? Enter boat or swim \n'
                            'Choice: ').lower()

        # If else statement for users input on second question
        if lake_choice == 'boat':
            print('\nYou made it to the other side!!')
            print('You see the treasure chest!!!')
            print('There is a bridge and a zip wire leading to it')
            after_lake_choice = input(
                'Would you like to walk the bridge or take the zip wire? Enter bridge or zip wire \n'
                'Choice: ').lower()

            # If else statement for users input on third question
            if after_lake_choice == 'bridge':
                print('\nYou narrowly made it before the bridge broke, Lucky!')
                print('You made it to the treasure chest!!!')
                treasure_choice = input('Would you like to open the chest or go home? Enter open or home \n'
                                        'Choice: ').lower()

                # If else statement for users input on fourth question
                if treasure_choice == 'open':
                    print('\nYou fund a donut inside! .. yay!')
                    print(f'You completed it in {attempts} attempts')
                else:
                    print('\nBye then')
                    game_over()

            else:
                print('\nI guess you havent been trained on how to use zip wires. Whoops')
                game_over()

        else:
            print('\nYou made it half way before becoming crocodile lunch :(')
            game_over()

    else:
        print('\nYou walked off a cliff, how silly')
        game_over()


# Calling game to start
game()
