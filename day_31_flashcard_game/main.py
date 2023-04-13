from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = '#70AEBA'

try:
    data = pd.read_csv('data/to_learn.csv')
except FileNotFoundError:
    data = pd.read_csv('data/french.csv')

to_learn = data.to_dict(orient='records')
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(background_img, image=card_front_img)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(background_img, image=card_back_img)


def known_words():
    to_learn.remove(current_card)
    to_learn_data = pd.DataFrame(to_learn)
    to_learn_data.to_csv('data/to_learn.csv',index=False)
    next_card()


window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
background_img = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, font=('Arial', 40, 'bold'))
canvas.grid(row=0, column=0, columnspan=2)

check = PhotoImage(file='images/right.png')
check_btn = Button(image=check, highlightthickness=0, command=known_words)
check_btn.grid(row=1, column=1)

cross = PhotoImage(file='images/wrong.png')
cross_btn = Button(image=cross, highlightthickness=0, command=next_card)
cross_btn.grid(row=1, column=0)

next_card()

window.mainloop()
