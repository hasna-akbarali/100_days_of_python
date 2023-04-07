from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

WHITE = 'white'

# -------- Password Generator ------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
               'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(symbols) for _ in range(randint(2, 4))]
    password_symbols = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+password_numbers+password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ------------ ADD PASSWORD ---------- #

def add():
    web = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(web) == 0 or len(password) == 0:
        messagebox.showerror(title='ERROR',message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=web,message=f'These are the details you have entered: \nEmail:'
                                                 f' {email}\nPassword: {password}\nIs it ok to save?')
        if is_ok:
            with open('data.txt', 'a') as f:
                f.write(f'{web} | {email} | {password}\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)




# ----------------- UI --------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo_png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_png)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg=WHITE)
website_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:", bg=WHITE)
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:", width=21, bg=WHITE)
password_label.grid(column=0, row=3)

generate_button = Button(text="Generate Password", width=21, bg=WHITE, highlightthickness=0,command=generate_password)
generate_button.grid(column=2, row=3, columnspan=2)
add_button = Button(text="Add", width=30, bg=WHITE, highlightthickness=0, command=add)
add_button.grid(column=1, row=4, columnspan=2)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
email_username_entry = Entry(width=35)
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(0, 'akbarali.hasna@gmail.com')
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

window.mainloop()
