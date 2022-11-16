# Importing modules
from turtle import Turtle
import random

# Constants
ball_directions = [45, 135, 225, 315]
LEFT_UP = 135
LEFT_DOWN = 225
RIGHT_UP = 45
RIGHT_DOWN = 315


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.random_heading = random.choice(ball_directions)
        self.x_move = 10
        self.y_move = 10
        self.penup()
        self.shape('circle')
        self.color('white')
        self.speed('slowest')

    def move_ball(self):
        """Makes the ball move in a diagonal up right motion, like so: / """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Makes the ball bounce on the y-axis"""
        self.y_move *= - 1

    def bounce_x(self):
        """Makes the ball bounce on the x-axis"""
        self.x_move *= -1

    def miss(self):
        """Resets the ball when the user misses it with the paddle"""
        self.goto(0, 0)
        self.x_move *= -1
