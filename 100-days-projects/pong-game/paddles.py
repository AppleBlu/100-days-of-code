# Importing modules
from turtle import Turtle

# Constants
PADDLE_1_COR = [(-900, 25), (-900, 5), (-900, -15), (-900, -35)]
PADDLE_2_COR = [(900, 25), (900, 5), (900, -15), (900, -35)]


class Paddle(Turtle):

    def __init__(self, position, color):
        super(Paddle, self).__init__()
        self.paddles = []
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color(color)
        self.goto(position)
        self.paddles.append(self)

    def go_up(self):
        """Makes the paddle go up"""
        new_y = self.ycor() + 70
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Makes the paddle go down"""
        new_y = self.ycor() - 70
        self.goto(self.xcor(), new_y)
