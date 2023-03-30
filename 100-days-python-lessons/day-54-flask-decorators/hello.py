# Importing modules
from flask import Flask
import time


# Making a decorator to change my html elements to underlined
def make_underline(function):
    def new_func():
        return "<u>" + function() + "</u>"

    new_func.__name__ = function.__name__  # now the wrapper function will be named as the name of function passed
    return new_func


# Making a decorator to change my html elements to bold
def make_bold(function):
    def new_func():
        return "<b>" + function() + "</b>"

    new_func.__name__ = function.__name__  # now the wrapper function will be named as the name of function passed
    return new_func


# Making a decorator to change my html elements to emphasised
def make_emphasis(function):
    def new_func():
        return "<em>" + function() + "</em>"

    new_func.__name__ = function.__name__  # now the wrapper function will be named as the name of function passed
    return new_func


# App is the Flask with the name of the file
app = Flask(__name__)


# if user is on the home page ("www.google.com/") then run the function
@app.route('/')
def hello_world():
    return 'Hello, World!'


# if user is on the home page ("www.google.com/username/Tom") then run the function
@app.route('/username/<name>')
def hello_name(name):
    return f'Hello, {name}!'


# if user is on the home page ("www.google.com/bye") then run the function
@app.route('/bye')
def bye():
    return '<h1 style="text-align: centre">Bye<h1>' \
           '<img src="https://media4.giphy.com/media/v1' \
           '.Y2lkPTc5MGI3NjExNTlmZjhiMzcyODNlMmIwODNjYjE3M2RmZTFkY2RkZTJkNjljYzQyYyZj' \
           'dD1n/c00LLteGojGfDHZXur/giphy.gif">'


# if user is on the home page ("www.google.com/decorated") then run the function
@app.route('/decorated')
@make_underline
@make_emphasis
@make_bold
def decorated():
    return "I am decorated"


# If name of the current file is "__main__" then run the app (By adding debug true I can edit the file, and it updates
# the website live without be having to reset it manually) I have to hit save after updating
if __name__ == "__main__":
    app.run(debug=True)


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
