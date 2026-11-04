from tkinter import *
import random
import pandas
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)

    if not to_learn:
        canvas.itemconfig(card_title, text="🎉", fill="black")
        canvas.itemconfig(card_word, text="All Done!", fill="black")
        return 

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text=["French"],fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background, image=front_img)
    flip_timer = window.after(3000,flip_card)

def flip_card():
    canvas.itemconfig(card_title, text=["English"],fill = "white")
    canvas.itemconfig(card_word, text=current_card["English"],fill = "white")
    canvas.itemconfig(card_background,image=card_eng_img)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(height=526,width=800)
front_img = PhotoImage(file="images/card_front.png")
card_eng_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400,263,image= front_img)
card_title = canvas.create_text(400,150,text="", font=("Ariel",40,"italic"))
card_word = canvas.create_text(400,263,text="", font=("Ariel",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img,command=next_card)
wrong_button.grid(row=1,column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img,command=is_known)
right_button.grid(row=1,column=1)
next_card()





window.mainloop()

