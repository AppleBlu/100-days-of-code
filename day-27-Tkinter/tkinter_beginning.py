import tkinter as tk

# Window creation
window = tk.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

# Label creation
my_label = tk.Label(text='I Am a Label!', font=('arial', 24, 'bold'))
my_label.pack(side='top')

tk.mainloop()
