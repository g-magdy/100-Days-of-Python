import tkinter, random, pandas
BACKGROUND_COLOR = "#B1DDC6"
THINKING_SECONDS = 3
chosen = {}
auto_turn = ""
LABEL_FONT = ("arial", 16, "normal")
# ------------------------------- READING DATA ------------------------------- #
try:
    yet_to_learn_df = pandas.read_csv("./data/words_to_learn.csv")
    yet_to_learn = yet_to_learn_df.to_dict(orient="records")
except FileNotFoundError:
    yet_to_learn_df = pandas.read_csv("./data/french_words.csv")
    yet_to_learn = yet_to_learn_df.to_dict(orient="records")
except pandas.errors.EmptyDataError:
    yet_to_learn_df = pandas.read_csv("./data/french_words.csv")
    yet_to_learn = yet_to_learn_df.to_dict(orient="records")
    
# ------------------------------- FUNCTIONS ------------------------------- #
def show_card():
    if len(yet_to_learn) > 0:
        global chosen, auto_turn
        if auto_turn != "":
            window.after_cancel(auto_turn) # to cancel previous clicks
        chosen = random.choice(yet_to_learn)
        canvas.itemconfig(language_text, text="French", fill="black")
        canvas.itemconfig(word_text, text=chosen["French"], fill="black")
        canvas.itemconfig(canvas_img, image=card_front)
        auto_turn = window.after(ms=THINKING_SECONDS*1000, func=show_answer)
    else:
        congrats()
    
def show_answer():
    global chosen, auto_turn
    chosen["French"]
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=chosen["English"], fill="white")
    canvas.itemconfig(canvas_img, image=card_back)
    
def dont_show_again():
    if len(yet_to_learn) != 0:
        yet_to_learn.remove(chosen)
        left_to_learn_counter.config(text=f"To be learned : {len(yet_to_learn)}")
        pandas.DataFrame(yet_to_learn).to_csv("./data/words_to_learn.csv", index=False)
        show_card()
    else:
        window.after_cancel(auto_turn)
        congrats()

def congrats():
    canvas.itemconfig(language_text, text="Congratulations :)")
    canvas.itemconfig(word_text, text="Completed 👏")
    
# ------------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()

window.title("Fashcard App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

right = tkinter.PhotoImage(file="./images/right.png")
wrong = tkinter.PhotoImage(file="./images/wrong.png")
card_front = tkinter.PhotoImage(file="./images/card_front.png")
card_back = tkinter.PhotoImage(file="./images/card_back.png")

right_button = tkinter.Button(image=right, highlightthickness=0, command=dont_show_again)
show_again_label = tkinter.Label(text="I got this", background=BACKGROUND_COLOR, highlightthickness=0, font=LABEL_FONT)
show_again_label.grid(row=2, column=1)
wrong_button = tkinter.Button(image=wrong, highlightthickness=0, command=show_card)
dont_show_again_label = tkinter.Label(text="I did not get this", background=BACKGROUND_COLOR, highlightthickness=0, font=LABEL_FONT)
dont_show_again_label.grid(row=2, column=0)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, font=("Calibri", 40, "italic"))
word_text = canvas.create_text(400, 263, font=("Calibri", 60, "bold"))

left_to_learn_counter = tkinter.Label(text=f"To be learned : {len(yet_to_learn)}"
                                      , font=LABEL_FONT, bg=BACKGROUND_COLOR, highlightthickness=0)
left_to_learn_counter.grid(row=3, column=0, columnspan=2)

canvas.grid(row=0, column=0, columnspan=2)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

show_card()

window.mainloop()
