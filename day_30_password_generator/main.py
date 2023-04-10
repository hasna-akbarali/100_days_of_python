from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT = ("Arial", 12)
BTN_FONT = ("Arial", 10)
DEFAULT_USERNAME = "akbarali.hasna@email.com"

WHITE = 'white'


# ---------------- Password Generator ------------------- #

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

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# --------------------- SEARCH PASSWORD ----------------------- #

def search():
    web = website_entry.get()
    try:
        with open('data.json', 'r') as file_data:
            data = json.load(file_data)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found')
    else:
            try:
                details = data[web]
            except KeyError:
                messagebox.showerror(title='Error', message='No details for this website exists')
            else:
                messagebox.showinfo(title=web,
                                    message=f"Email : {details['Email']}\nPassword: {details['Password']}")
            finally:
                website_entry.delete(0,END)


# ---------------------- ADD PASSWORD ------------------------- #

def add():
    web = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()
    new_data = {
        web: {
            "Email": email,
            "Password": password,
        }
    }

    if len(web) == 0 or len(password) == 0:
        messagebox.showerror(title='ERROR', message="Please don't leave any fields empty!")

    else:
        # is_ok = messagebox.askokcancel(title=web,message=f'These are the details you have entered: \nEmail:'
        #                                          f' {email}\nPassword: {password}\nIs it ok to save?')
        try:
            with open('data.json', 'r') as data_f:
                # f.write(f'{web} | {email} | {password}\n')
                data = json.load(data_f)
                data.update(new_data)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# # ----------------- UI --------------- #

# main window setup
root = Tk()
root.title("Password Manager")
root.geometry("500x400")
root.resizable(False, False)

# top frame
top_frame = Frame(root)
top_frame.pack()
# canvas
canvas = Canvas(top_frame, width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
# the top frame only has a single element, so a simple pack() works just fine
canvas.pack(padx=20, pady=20)

# bottom frame
bottom_frame = Frame(root)
bottom_frame.pack()
# left column
website_lbl = Label(bottom_frame, text="Website:", font=FONT, width=16)
website_lbl.grid(row=0, column=0, pady=4)
email_lbl = Label(bottom_frame, text="Email/Username:", font=FONT, width=16)
email_lbl.grid(row=1, column=0, pady=4)
password_lbl = Label(bottom_frame, text="Password:", font=FONT, width=16)
password_lbl.grid(row=2, column=0, pady=4)

# middle+right column, span across 2 columns
website_entry = Entry(bottom_frame, font=FONT, width=16)
website_entry.grid(row=0, column=1, padx=8, pady=4)
# to make the cursor active in the field
website_entry.focus()
email_username_entry = Entry(bottom_frame, font=FONT, width=32)
email_username_entry.grid(row=1, column=1, columnspan=2, pady=4)
email_username_entry.insert(0, DEFAULT_USERNAME)
add_btn = Button(bottom_frame, text="Add", font=BTN_FONT, bg="#ddd", width=32, relief="raised",
                 command=add)
add_btn.grid(row=3, column=1, columnspan=2, pady=8)
search_btn = Button(bottom_frame, text="Search", font=BTN_FONT, width=15, relief="raised",
                      command=search)
search_btn.grid(row=0, column=2, padx=7, pady=4)
# middle column
password_entry = Entry(bottom_frame, font=FONT, width=16)
password_entry.grid(row=2, column=1, padx=8, pady=4)

# right column
password_btn = Button(bottom_frame, text="Generate Password", font=BTN_FONT, width=15, relief="raised",
                      command=generate_password)
password_btn.grid(row=2, column=2, padx=7, pady=4)
# main loop
root.mainloop()
