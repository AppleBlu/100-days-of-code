import random
import turtle
from turtle import Turtle
from turtle import Screen

is_race_on = False
screen = Screen()
screen.setup(height=500, width=700)
user_1_name = screen.textinput(title='User 1', prompt='Enter your name')
user_1_bet = screen.textinput(title='User 1', prompt='Which turtle will win the race? Enter a colour: ')
print(user_1_bet)
user_2_name = screen.textinput(title='User 2', prompt='Enter your name')
user_2_bet = screen.textinput(title='User 2', prompt='Which turtle will win the race? Enter a colour: ')
print(user_2_bet)

y_coordinates = [200, 150, 100, 50, 0, -50]
turtle_colours = ['red', 'blue', 'green', 'pink', 'orange', 'purple']
all_turtles = []


for turtle_index in range(0, 6):
    race_turtle = Turtle()
    race_turtle.penup()
    race_turtle.goto(x=-300, y=y_coordinates[turtle_index])
    race_turtle.shape('turtle')
    race_turtle.color(turtle_colours[turtle_index])
    all_turtles.append(race_turtle)


if user_1_bet and user_2_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 325:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_1_bet:
                print(f'The winning turtle was {winning_turtle}, Congrats {user_1_name}!!!')
            elif winning_turtle == user_2_bet:
                print(f'The winning turtle was {winning_turtle}, Congrats {user_2_name}!!!')
            else:
                print(f'No one won. The winning turtle was {winning_turtle}')
        random_distance = random.randint(0, 5)
        turtle.forward(random_distance)
screen.exitonclick()
