
import tkinter
import pandas as pd
import random



BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}
# ---------------------------- ERROR HANDLING  ------------------------------- #

try:
    # Try to load saved words
    data = pd.read_csv("data/words_to_learn.csv")

except FileNotFoundError:
    # If file doesn't exist, use original data
    original_data = pd.read_csv("data/korean_words.csv")

    # Convert data into a list of dictionaries
    to_learn = original_data.to_dict(orient="records")

else:
    # If saved file exists, use it
    to_learn = data.to_dict(orient="records")

# ---------------------------- RANDOM WORDS GENERATION ------------------------------- #

#instead of reading the words from korean_words its more reliable to read it from words_to_learn
# so that the word are present in words_to_learn are shown to us
# data = pd.read_csv("data/korean_words.csv")

data = pd.read_csv("data/words_to_learn.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)



def next_card():
    global current_card ,flip_timer
    # Cancel the previously scheduled 3-second flip timer.
    # Without this, the old timer would still run and flip the card
    # even after the user has already clicked and moved to the next card.
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    print(current_card["KOREAN"])

    #changing the font black as the card flips to front
    canvas.itemconfig(card_title, text="KOREAN", font=("arial",40,"bold"),fill="black")
    canvas.itemconfig(card_word, text=current_card["KOREAN"], font=("arial",40,"bold"),fill="black")

    # Again changing the card_back_image to card_front_image so that game continues
    canvas.itemconfig(card_background, image=card_front_img)

    flip_timer = window.after(3000, flip_card)



# ---------------------------- CARD FLIP ------------------------------- #

def flip_card():
        print(current_card["ENGLISH"])

        # configuring title and description text for back side which has english meaning
        canvas.itemconfig(card_title, text="ENGLISH", font=("arial",40,"bold"),fill="white")
        canvas.itemconfig(card_word, text=current_card["ENGLISH"], font=("arial",40,"bold"),fill="white")

        # configuring front image to back image
        canvas.itemconfig(card_background, image=card_back_img)

# ---------------------------- REMOVING KNOWN WORDS FROM DICT ------------------------------- #

def is_known():
    to_learn.remove(current_card)     # Remove the learned card
    print(len(to_learn))              # Check remaining cards
    data = pd.DataFrame(to_learn)     # Convert the list into a DataFrame
    # Index = false is used to Prevent pandas from saving row numbers as an extra column
    # because (every time new index is added automatically)
    data.to_csv("data/words_to_learn.csv",index=False)

    next_card()



# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

# after is made under variable to call it globally in other function
flip_timer = window.after(3000, flip_card)

#canvas
canvas = tkinter.Canvas(window,background=BACKGROUND_COLOR,width=800,height=526,highlightthickness=0)

#inserting card fron and card back image
card_front_img = tkinter.PhotoImage(file="images/card_front.png")
card_back_img = tkinter.PhotoImage(file="images/card_back.png")

#setting card background as card front  image [configured to card back image in flip_card() function]
card_background = canvas.create_image(400,263,image=card_front_img)

card_title =canvas.create_text(400,150,text="Title",font=("arial",40,"italic"),fill="black")
card_word = canvas.create_text(400,263,text="Description",font=("arial",40,"bold"),fill="black")

canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0,column=0)


#button
wrong_png = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_png,highlightthickness=0,command=flip_card)
wrong_button.grid(row=1,column=0,sticky="w")

right_png = tkinter.PhotoImage(file="images/right.png")
#Is known is in the command because is_known does calls next card inside it
right_button = tkinter.Button(image=right_png,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=0,columnspan=2,sticky="e")



next_card()













window.mainloop()