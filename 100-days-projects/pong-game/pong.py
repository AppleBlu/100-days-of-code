# Importing modules
from turtle import Screen
from paddles import Paddle
from ball import Ball
from interface import Scoreboard
import time

# Initializing the Screen
screen = Screen()


# The game start up
def game():

    # Screen setup
    screen.clear()
    screen.tracer(0)
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title('PONG')

    # Initializing the Scoreboard and Ball
    scoreboard = Scoreboard()
    ball = Ball()

    # Creating the left and right paddles
    l_paddle = Paddle(position=(-350, 0), color='blue')
    r_paddle = Paddle(position=(350, 0), color='pink')

    # Allowing the users to enter commands
    screen.listen()
    screen.onkey(l_paddle.go_up, 'w')
    screen.onkey(l_paddle.go_down, 's')
    screen.onkey(r_paddle.go_up, 'Up')
    screen.onkey(r_paddle.go_down, 'Down')

    game_is_on = True
    while game_is_on:
        time.sleep(0.125)
        screen.update()
        ball.move_ball()

        # Checking if the ball hits the bottom or top and makes it bounce
        if ball.ycor() > 289 or ball.ycor() < -289:
            ball.bounce_y()

        # Checking if ball misses the right paddle and resets the ball and gives the left player a point
        if ball.xcor() > 390 and ball.distance(r_paddle) > 50:
            ball.miss()
            scoreboard.l_score()

        # Checking if ball misses the left paddle and resets the ball and gives the right player a point
        elif ball.xcor() < -400 and ball.distance(l_paddle) > 50:
            ball.miss()
            scoreboard.r_score()

        # Checking if the ball hits either the left or right paddles and makes it bounce off of them
        elif ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < -320 and ball.distance(l_paddle) < 50:
            ball.bounce_x()


# game setup
game()
screen.exitonclick()
