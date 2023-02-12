# Normal function
def add(a, b, c):
    return a + b + c


"""Can be called like so:
add()"""


# Function with default arguments
def add2(a=1, b=2, c=3):
    return a + b + c


"""Can be called like so:
add2()
or
add2(2, 3, 1)
or 
add2(a=1, c=3, b=2)
or
add2(c=3)"""


# Function with unlimited positional arguments
def add3(*args):
    math_sum = 0
    for arg in args:
        math_sum += arg
    return math_sum


# Can call it with however many arguments you want
print(add3(1, 2, 3, 4))
print((add3(1, 34, 12, 342, 32, 1)))
print((add3(1, 2)))


# Function with unlimited positional keyword arguments
def add4(number, **kwargs):
    # Prints all the keywords to values as a dict
    print(kwargs)
    # Prints the value of the key 'add'
    print(kwargs['add'])
    # Loops through the items in the dict and prints each key and value
    for key, value in kwargs.items():
        print(key)
        print(value)

    # Calculations using the keyword arguments
    number += kwargs['add']
    number -= kwargs['minus']
    return number


# Calling the function with keys and values
print((add4(2, add=1, minus=2)))


# Using unlimited positional keyword arguments in a class
class Car:

    def __init__(self, **kwargs):
        self.make = kwargs['make']
        self.model = kwargs['model']
        # Using .get() doesn't throw an error if you don't provide a value for it
        # Still works the same
        self.colour = kwargs.get('colour')


my_car = Car(model='Juke', make='Nissan')

print(my_car.make)
print(my_car.model)
