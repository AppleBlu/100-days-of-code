# Importing the whole tkinter module
from tkinter import *


def miles_to_km():
    miles_number = float(miles.get())
    km_number = round(miles_number * 1.689)
    km_result_label.config(text=f'{km_number}')


# Window creation
window = Tk()
window.title('Mile to Km Converter')
window.minsize(500, 150)
window.config(padx=30, pady=30)

# Button creation
calculate_button = Button(text='Calculate', command=miles_to_km)
calculate_button.grid(row=2, column=1)

# Label creation
equal_label = Label(text='Is equal to:', font=('arial', 13, 'italic'))
equal_label.grid(row=1, column=0)

miles_label = Label(text='Miles', font=('arial', 20))
miles_label.grid(row=0, column=2)

km_label = Label(text='Km', font=('arial', 20))
km_label.grid(row=1, column=2)

km_result_label = Label(text='0')
km_result_label.grid(row=1, column=1)

# Entry creation
miles = Entry(width=7)
miles.insert(END, string='0')
miles.grid(row=0, column=1)


window.mainloop()
