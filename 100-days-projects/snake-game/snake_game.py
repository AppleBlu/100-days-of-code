# Importing modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time


def game():
    # Creating the screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('My Snake Game')
    # Asking the user to enter a game type
    game_type = screen.textinput(title='Game Type', prompt='Enter Endless or Mission').lower()
    screen.clear()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('My Snake Game')
    screen.tracer(0)

    # Creating the snake, food and score instances
    snake = Snake()
    food = Food()
    score = Score()
    score.game_type = game_type

    # If statement to check what game mode the user picked
    if game_type == 'mission':
        score.goal = 25
        score.score_write_mission()

    else:
        # Writing the score
        score.score_write_endless()

    # Allowing the user to input directions for the snake
    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')

    # Setting game_is_on to True
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)

        # Moving the snake
        snake.move()

        # If statement to check if the snake has hit the food
        if snake.head.distance(food) < 20:
            food.refresh()
            score.update_score(game_type, score=score.score)
            snake.extend()
            if score.score == score.goal:
                score.game_win()
                game_is_on = False

        # If statement checking to see if the snake has gone out of bounds
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.reset()
            snake.reset_snake()

        # If statement to check if the snake head has hit any part of the snake body/tail
        for block in snake.blocks[1:]:
            if snake.head.distance(block) < 10:
                score.reset()
                snake.reset_snake()

    if not game_is_on:
        game()

    screen.exitonclick()


game()
