# Importing modules
from turtle import Turtle

# Constants for initial snake block positions, move distance and degrees for up, down, left and right
BLOCK_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Class Snake to build and move the snake
class Snake:

    def __init__(self):
        self.blocks = []
        self.make_snake()
        self.head = self.blocks[0]

    def make_snake(self):
        """Adds the initial blocks of the snake"""
        for position in BLOCK_POSITIONS:
            self.add_block(position)

    def move(self):
        """Makes the blocks of the snake behind the head block follow the head when the head changes direction"""
        for block in range(len(self.blocks) - 1, 0, -1):
            new_x = self.blocks[block - 1].xcor()
            new_y = self.blocks[block - 1].ycor()
            self.blocks[block].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """When "up" is entered the heading changes to the degrees held in the constant UP"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """When "down" is entered the heading changes to the degrees held in the constant DOWN"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """When "left" is entered the heading changes to the degrees held in the constant LEFT"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """When "right" is entered the heading changes to the degrees held in the constant RIGHT"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_block(self, position):
        """Used with make_snake()"""
        new_block = Turtle('square')
        new_block.speed('slowest')
        new_block.shapesize(0.8)
        new_block.color('pink')
        new_block.penup()
        new_block.goto(position)
        self.blocks.append(new_block)

    def extend(self):
        """Adds one block to the end of the snake"""
        self.add_block(self.blocks[-1].position())

    def reset_snake(self):
        for block in self.blocks:
            block.goto(1000, 1000)
        self.blocks.clear()
        self.make_snake()
        self.head = self.blocks[0]
