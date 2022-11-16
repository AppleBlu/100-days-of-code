# Importing modules
from turtle import Turtle

# Constants for a set font and alignment used for the score display
ALIGNMENT = 'center'
FONT = ('arial', 13, 'bold')


# Class Score that inherits the Turtle class
class Score(Turtle):

    # Methods and attributes of the score
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt', mode='r') as data_file:
            self.high_score = int(data_file.read())
        self.goal = 1000
        self.game_type = ''

    def score_write_mission(self):
        """Writes the score at the top of the screen when mission is selected by the user"""
        self.penup()
        self.hideturtle()
        self.color('red')
        self.goto(x=0, y=280)
        self.write(arg=f'Score: {self.score}/{self.goal} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def score_write_endless(self):
        """Writes the score at the top of the screen when endless is selected by the user"""
        self.penup()
        self.hideturtle()
        self.color('red')
        self.goto(x=0, y=280)
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def update_score(self, game_t, score = 0):
        """Updates the score by incrementing it by 1"""
        if game_t == 'mission':
            self.clear()
            self.score = score
            self.score += 1
            if self.score > self.high_score:
                with open('high_score.txt', mode='w') as data_file:
                    data_file.write(str(self.score))
                with open('high_score.txt', mode='r') as data_file:
                    self.high_score = int(data_file.read())
            self.write(arg=f'Score: {self.score}/{self.goal} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)
        else:
            self.clear()
            self.score = score
            self.score += 1
            if self.score > self.high_score:
                with open('high_score.txt', mode='w') as data_file:
                    data_file.write(str(self.score))
                with open('high_score.txt', mode='r') as data_file:
                    self.high_score = int(data_file.read())
            self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset(self):
        """Resets the score to 0"""
        if self.score > self.high_score:
            with open('high_score.txt', mode='w') as data_file:
                data_file.write(str(self.score))
            with open('high_score.txt', mode='r') as data_file:
                self.high_score = int(data_file.read())
        self.score = 0
        self.update_score(game_t=self.game_type, score=-1)
        self.score = 0

    # def game_over(self):
    #     """Prints a game over message in the center of the screen"""
    #     self.goto(0, 100)
    #     self.color('white')
    #     self.write(f'Game Over\nScore: {self.score}', align=ALIGNMENT, font=('Courier', 25, 'bold'))

    def game_win(self):
        """Prints a game win message in the center of the screen"""
        self.goto(0, 100)
        self.color('white')
        self.write(f'Mission Complete!!!\nScore: {self.score}', align=ALIGNMENT, font=('Courier', 25, 'bold'))
