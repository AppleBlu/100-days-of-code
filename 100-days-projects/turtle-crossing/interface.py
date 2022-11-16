from turtle import Turtle
import time

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 0
        self.penup()
        self.color('black')
        self.hideturtle()
        self.next_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER\nLevel {self.level}', False, 'center', FONT)

    def round_win(self):
        self.goto(0, 0)
        self.write('ROUND WIN!!!', False, 'center', FONT)
        time.sleep(2)
        self.clear()

    def next_level(self):
        self.clear()
        self.level += 1
        self.goto(-200, 250)
        self.write(f'Level {self.level}', False, 'center', FONT)

