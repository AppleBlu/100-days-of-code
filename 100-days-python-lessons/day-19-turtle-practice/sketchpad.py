from turtle import Turtle
from turtle import Screen

tim = Turtle()
screen = Screen()

tim.pensize(5)


def move_forward():
    tim.forward(10)


def move_back():
    tim.backward(10)


def turn_right():
    tim.right(45)


def turn_left():
    tim.left(45)


screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)
screen.onkey(key='c', fun=tim.clear)
screen.exitonclick()
