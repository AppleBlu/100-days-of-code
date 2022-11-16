import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from interface import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
counter = 0
while game_is_on:
    counter += 1
    time.sleep(0.06)
    screen.update()
    car.make_cars()
    car.drive()
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 300:
        scoreboard.round_win()
        scoreboard.next_level()
        player.reset_player()
        car.increase_car_speed()

screen.exitonclick()
