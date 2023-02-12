import random
from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 2

    def make_cars(self):
        random_chance = random.randint(1, 10)
        if random_chance == 1:
            car = Turtle('square')
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-230, 250)
            car.goto(300, random_y)
            car.shapesize(stretch_wid=1, stretch_len=2)
            self.all_cars.append(car)

    def drive(self):
        for car in self.all_cars:
            car.back(self.car_speed)

    def increase_car_speed(self):
        self.car_speed += 1


