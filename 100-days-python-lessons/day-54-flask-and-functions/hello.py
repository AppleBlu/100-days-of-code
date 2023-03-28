# Importing modules
from flask import Flask
import time

# # App is the Flask with the name of the file
# app = Flask(__name__)
#
#
# # if user is on the home page ("www.google.com/") then run the function
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'
#
#
# # If name of the current file is "__main__" then run the app
# if __name__ == "__main__":
#     app.run()


# Making a function decorator
def speed_calc_decorator(function):  # Takes in a function
    def wrapper_function():  # Function wrapper to hold the code to run
        time_now = time.time()  # Getting hold of the time now in seconds
        function()  # Calling the function passed as an argument in the original function
        time_after = time.time()  # Getting hold of the time now in seconds
        print(f"{function.__name__}: {time_after - time_now}")  # Printing the function name and how long it took to run

    return wrapper_function()  # Returning the wrapper function


# Adding the decorator to this function
@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        var = i * i


# Adding the decorator to this function
@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        var = i * i

