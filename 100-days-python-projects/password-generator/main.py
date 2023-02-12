# Importing modules
import random

# List of all letters, symbols and numbers
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Printing welcome message
print("Welcome to the PyPassword Generator!\n")

# Asking the user how many of each char type they want
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Assigning 3 variables to empty strings
letter_str = ''
symbol_str = ''
number_str = ''

# 3 for loops to get random chars from each char type related to users input
for letter in range(nr_letters):
    letter_str = letter_str + random.choice(letters)

for symbol in range(nr_symbols):
    symbol_str = symbol_str + random.choice(symbols)

for number in range(nr_numbers):
    number_str = number_str + random.choice(numbers)

# Combining the 3 strings
password_ordered = letter_str + symbol_str + number_str
# Making the combined string into a list
password_ordered_list = list(password_ordered)

# Shuffling the list
random.shuffle(password_ordered_list)
# Assigning the result to final_password
final_password = ''.join(password_ordered_list)

# Printing the password
print(f'\nPassword generated: {final_password}')
