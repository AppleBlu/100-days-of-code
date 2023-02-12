# Importing modules
import art

# List that holds the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

# Printing the logo for the program
print(art.logo)


# Function that holds the application
def app():
    """Will run the app"""
    # Asking the user multiple questions
    direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    new_shift = shift % 27

    # Function that encodes or decodes the users inputs
    def caesar(start_text, shift_amount, cipher_direction):
        """Encodes or decodes the users input and prints the result"""
        end_text = ''

        if cipher_direction == 'decode':
            shift_amount *= -1
        for char in start_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char

        # Printing the display
        print(f'The {cipher_direction}d text is {end_text}')

    # Calling the function
    caesar(text, new_shift, direction)


# Calling the application
app()

# Asking the user if they would like to restart the application
restart = input('\nWhat you like to restart (Y/N) \n: ').lower()

# If statement for diff restart inputs
if restart == 'y':
    app()
elif restart == 'n':
    print('Good bye')
    exit()
