# Importing modules
from turtle import Turtle
import random

# Constant that holds a list of colours
COLOURS = ['pink', 'orange', 'red', 'blue', 'green', 'purple']


# Class Food that inherits class Turtle
class Food(Turtle):

    # Methods and attributes of the food
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.speed('fastest')
        self.color(random.choice(COLOURS))
        self.random_x = random.randint(-260, 260)
        self.random_y = random.randint(-260, 260)
        self.goto(x=self.random_x, y=self.random_y)
        self.refresh()

    def refresh(self):
        """Refreshes the food to a new random location"""
        self.color(random.choice(COLOURS))
        self.random_x = random.randint(-260, 260)
        self.random_y = random.randint(-260, 260)
        self.goto(x=self.random_x, y=self.random_y)
