# Importing modules
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
# Colours
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Variables
reps = 0
clock_timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    """Resets the timer, text at the top to "Timer". And removes the checkmarks"""
    global reps
    reps = 0
    # Pauses the timer
    window.after_cancel(clock_timer)
    # Resets the title to Timer
    timer.config(text='Timer')
    # Resets the timer
    canvas.itemconfig(timer_text, text='00:00')
    # Removes checkmarks
    tick.config(text='')


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    """Strats the timer with the relevant time required"""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If statement to check what cycle the timer is on and displays the correct time
    if reps % 8 == 0:
        timer.config(text='Long Break', fg=GREEN)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        timer.config(text='Short Break', fg=PINK)
        countdown(short_break_sec)
    else:
        timer.config(text='Work', fg=RED)
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    """Shows a timer and checkmarks for each work cycle"""
    global clock_timer
    count_min = math.floor(count / 60)
    count_seconds = count % 60

    if count_seconds < 10:
        count_seconds = f'0{count_seconds}'

    # Showing the timer
    canvas.itemconfig(timer_text, text=f'{count_min}:{count_seconds}')
    if count > 0:
        clock_timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps / 2)
        # Adding checkmarks for each work cycle
        for _ in range(work_sessions):
            marks += '✅'
        tick.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# Window creation
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas creation
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 110, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', font=('DS-Digital', 26, 'bold'), fill='white')
canvas.grid(row=1, column=1)


# Button creation
def start_action():
    start_timer()


start = Button(text="Start", command=start_action, highlightthickness=0)
start.grid(row=2, column=0)

reset = Button(text='Reset', command=reset_timer, highlightthickness=0)
reset.grid(row=2, column=2)

# Label creation
timer = Label(text='Timer', font=('Kalam', 26, 'bold'), fg=RED, bg=YELLOW)
timer.grid(row=0, column=1)

tick = Label(fg=RED, bg=YELLOW, font=('arial', 30, 'bold'))
tick.grid(row=3, column=1)

window.mainloop()
