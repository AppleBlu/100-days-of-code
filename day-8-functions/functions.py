name = input('\nEnter your name: ')
location = input('Enter your location: ')


def greet():
    print('\nHello')
    print('and')
    print('Welcome')


def greet_with_name(user_name):
    print(f'\nHello {user_name}')
    print('and')
    print('Welcome')


def greet_with(user_name, user_location):
    print(f'\nHello {user_name} from {user_location}')
    print('and')
    print('Welcome')


greet()
greet_with_name(name)
greet_with(user_location=location, user_name=name)
