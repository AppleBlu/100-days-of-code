# Importing modules
from tkinter import *
from tkinter import messagebox
from random import shuffle, choice, randint
import json
import pyperclip

# Colours
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Timmana"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    """Generates a random secure password"""
    password_entry.delete(0, END)
    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letter_list + symbol_list + number_list
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """Saves the login info to a text file"""
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()
    new_data = {
        website_data: {
            'Email': email_data,
            'Password': password_data
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title='Oops', message='Please dont leave any fields empty')

    else:
        is_ok = messagebox.askokcancel(title=website_data, message=f'These are the details entered: \nEmail:'
                                                                   f' {email_data} \nPassword:'
                                                                   f' {password_data} \nIs this correct?')

        if is_ok:
            try:
                with open(file='/media/tom/0840-502D/new-folder/data_file.json', mode='r') as data_file:
                    data = json.load(data_file)

            except:
                with open(file='/media/tom/0840-502D/new-folder/data_file.json', mode='w') as data_file:
                    json.dump(new_data, data_file, indent=4)

            else:
                data.update(new_data)
                with open(file='/media/tom/0840-502D/new-folder/data_file.json', mode='w') as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    search_context = website_entry.get()
    try:
        with open(file='/media/tom/0840-502D/new-folder/data_file.json', mode='r') as data_file:
            data = json.load(data_file)
            try:
                specific_email = data[search_context]['Email']
                specific_password = data[search_context]['Password']
                messagebox.showinfo(title=search_context, message=f'Email: {specific_email}\nPassword: '
                                                                  f'{specific_password}')
                pyperclip.copy(specific_password)
            except KeyError:
                messagebox.showerror(title=search_context, message='No details for the website exists')
    except:
        messagebox.showerror(title=search_context, message='No data file found')


# ---------------------------- UI SETUP ------------------------------- #

# Window creation
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Canvas creation
canvas = Canvas(width=200, height=200)
password_manager_img = PhotoImage(file='logo.png')
logo = canvas.create_image(100, 100, image=password_manager_img)
canvas.grid(row=0, column=1)

# Label creation
website_label = Label(text='Website: ', font=(FONT_NAME, 15))
website_label.grid(row=1, column=0)

email_username_label = Label(text='Email/Username: ', font=(FONT_NAME, 15))
email_username_label.grid(row=2, column=0)

password_label = Label(text='Password: ', font=(FONT_NAME, 15))
password_label.grid(row=3, column=0)

# Entry creation
website_entry = Entry(width=24)
website_entry.insert(END, string="")
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.insert(END, string="")
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'appleyard1818@gmail.com')

password_entry = Entry(width=24)
password_entry.insert(END, string="")
password_entry.grid(row=3, column=1)

# Button creation
generate_password_button = Button(text="Generate", highlightthickness=0, command=generate_password)
generate_password_button.grid(row=3, column=2, columnspan=1)

search_button = Button(text="Search", highlightthickness=0, command=find_password, width=7)
search_button.grid(row=1, column=2, columnspan=1)

add_button = Button(text="Add", highlightthickness=0, width=32, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
