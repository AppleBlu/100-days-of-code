import random
import turtle
from turtle import Turtle, Screen
from random import choice

tim = Turtle()

list_of_colours = ['blue', 'red', 'black', 'yellow', 'pink', 'brown', 'orange', 'purple']

lst_of_moving_methods = [
    tim.forward,
    tim.backward
]

lst_of_turning_methods = [tim.right, tim.left]

lst_of_directions = [0, 90, 180, 270]


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colours = (r, g, b)
    return random_colours


# Turtle design
tim.shape('classic')
tim.color('black')
tim.speed(15)

# Pen design
tim.pensize(3)


# Turtle draws a square
def draw_square():
    for movement in range(4):
        tim.forward(100)
        tim.right(90)


# Turtle draws a triangle
def draw_triangle():
    for movement in range(3):
        tim.forward(100)
        tim.right(120)


def patten():
    counter = 3
    while counter < 10:
        colour_choice = choice(list_of_colours)
        list_of_colours.remove(colour_choice)
        tim.color(colour_choice)
        for movement in range(counter):
            tim.forward(50)
            tim.right(360 / counter)
            tim.forward(50)
        counter += 1


def advanced_patten():
    tim.circle(100, 360, 50)
    tim.degrees(20)
    tim.circle(100, 360, 50)


# Draw a dotted line
def dotted_line():
    for line in range(20):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()


def random_walk():
    for movement in range(200):
        tim.setheading(choice(lst_of_directions))
        tim.color(choice(list_of_colours))
        tim.forward(50)


# # Drawing patten
# patten()
#
# # Drawing a dotted line
# dotted_line()
#
# # Random walk
# random_walk()


def circle_spiral():
    for circle in range(100):
        tim.circle(100, 355, 10)
        tim.color(choice(list_of_colours))
        tim.left(10)


circle_spiral()
# Screen
my_screen = Screen()
my_screen.screensize(9000, 9000)
my_screen.exitonclick()
