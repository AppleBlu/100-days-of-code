# Importing modules and files
import random
import hangman_words
import hangman_art

# Assigning end_of_game to False
end_of_game = False
# Assigning lives to 6
lives = 6
# Assigning chosen_word to a random word from word_list
chosen_word = random.choice(hangman_words.word_list)
# Assigning word_length to the length of chosen_word
word_length = len(chosen_word)
# Assigning guesses to an empty list
guesses = []

# printing title art.py
print(hangman_art.logo)
# Printing the beginning hangman image
print(hangman_art.stages[6])

# Create blanks in display
display = []
for _ in range(word_length):
    display += "_"

# While loop to test if the game has ended
while not end_of_game:
    # Asking the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check users guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            # Adding it to display if correct
            display[position] = letter

    # Printing string if user has already guessed that letter
    if guess in guesses:
        print('You already guessed that')
        # Ignoring the rest of the code in the while loop
        continue

    # Appending guess to list guesses
    guesses.append(guess)

    # Printing string if the guess is not in the word
    if guess not in chosen_word:
        lives -= 1
        print('Letter is not in the word')

    # Printing the display
    print(f"{' '.join(display)}")

    # Checking if the display list is full
    if "_" not in display:
        end_of_game = True
        print("You win.")
    # Checking if the user has run out of lives
    elif lives == 0:
        end_of_game = True
        print('You lose')
        print(f'The word was {chosen_word}')

    # Printing the hangman image related to users lives
    print(hangman_art.stages[lives])
