# Importing modules
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Prints the scores at the top"""
        self.goto(-100, 185)
        self.write(self.left_score, align='center', font=('courier', 75, 'normal'))
        self.goto(100, 185)
        self.write(self.right_score, align='center', font=('courier', 75, 'normal'))

    def l_score(self):
        """Adds 1 to the left players score"""
        self.left_score += 1
        self.clear()
        self.update_scoreboard()

    def r_score(self):
        """Adds 1 to the right players score"""
        self.right_score += 1
        self.clear()
        self.update_scoreboard()
