import tkinter
import time
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
FONT = (FONT_NAME, 36, "bold")
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg=YELLOW)

timer_lbl = tkinter.Label(text="Timer", font=FONT, foreground=GREEN, background=YELLOW, highlightthickness=0)
timer_lbl.config(padx=10, pady=10)
timer_lbl.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
ph_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=ph_img)
canvas.create_text(100, 130, text="00:00", fill="white", font=FONT)
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 14))
start_button.config(padx=10, pady=10)
start_button.grid(row=2, column=0)

checkmark = tkinter.Label(text="✔", fg=RED, font=(FONT_NAME, 20), bg= YELLOW,  highlightthickness=0)
checkmark.config(padx=10, pady=10)
checkmark.grid(row=2, column=1)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 14))
reset_button.config(padx=10, pady=10)
reset_button.grid(row=2, column=2)

window.mainloop()