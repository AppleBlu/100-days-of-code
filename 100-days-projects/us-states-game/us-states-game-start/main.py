# Importing modules
import turtle
import pandas

# Creating the screen
screen = turtle.Screen()
screen.title('Us State Quiz Game')
screen.setup(height=500, width=720)
screen.bgcolor('black')
image = 'blank_states_img.gif'
screen.addshape(image)

# Adding the map
turtle.shape(image)

# reading and retrieving data from 50_states.csv
state_data = pandas.read_csv('50_states.csv')
states = state_data['state'].to_list()

correct_guesses = []

game_is_on = True
while game_is_on:
    # Asking the user to guess
    answer_state = screen.textinput(title=f'Guess The State {len(correct_guesses)}/50',
                                    prompt='Name a US State').title()

    # If the state they guessed is in the states and not already guessed:
    if answer_state in states and answer_state not in correct_guesses:
        correct_guesses.append(answer_state)
        state = turtle.Turtle()
        state.color('black')
        state.penup()
        state.hideturtle()
        # Getting the row related to the state
        state_row = state_data[state_data.state == answer_state]
        # Getting the x and y cors of the state
        state_x = state_row['x']
        state_y = state_row['y']
        state.goto(int(state_x), int(state_y))
        state.write(answer_state, align='center')

    # Checking if the user guessed all the states
    if len(correct_guesses) == 50:
        game_is_on = False
        win = turtle.Turtle()
        win.penup()
        win.hideturtle()
        win.color('black')
        win.write('Wow you guessed them all!!', align='center')


def get_mouse_click_coordinate(x, y):
    """Prints out the x and y cors when the mouse is clicked"""
    print(x, y)


turtle.onscreenclick(get_mouse_click_coordinate)

turtle.mainloop()
