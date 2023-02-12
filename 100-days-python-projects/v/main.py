from turtle import *

turtle = Turtle()
# hideturtle()

screen = Screen()

turtle.color("red")
turtle.speed("slowest")
turtle.hideturtle()
turtle.penup()
screen.delay(50)
turtle.write("Will you", align="center", font=("Kalam", 30))
turtle.right(90)
turtle.forward(50)
turtle.write("be my", align="center", font=("Kalam", 30))
turtle.forward(50)
turtle.write("valentine?", align="center", font=("Kalam", 30))
turtle.forward(100)
image = "images.gif"
turtle.showturtle()
screen.addshape(image)
turtle.shape(image)
answer = screen.textinput("", "Yes or no")

if answer == "yes":
    screen.clear()
    turtle.left(90)
    turtle.forward(200)
    turtle.write("YAYYY!", font=("Kalam", 30))

screen.mainloop()
