# Printing a welcome message
print('Welcome to the band name generator')

# Asking the user to enter what city they grow up in and a pet name
city = input('What city did you grow up in? \nCity: ')  # Assigning city to the users input
pet = input('Enter the name of a pet \nPet:')  # Assigning city to the users input

# Defining band_name to equal city + pet
band_name = city + ' ' + pet
# Printing the band name
print(f'\nYour band name is {band_name}. Or you could have {band_name}' + '\'s')
