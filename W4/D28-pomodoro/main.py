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
reps = 0
checks = 0
counting = ""
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps, checks
    window.after_cancel(counting)
    reps = 0
    checks = 0
    checkmark.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    timer_lbl.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0 and reps > 0:
        timer_lbl.config(text="Break", fg=RED)
        count_down(4) # long break
    elif reps % 2 == 1:
        timer_lbl.config(text="Work", fg=GREEN)
        count_down(5) # work
    else:
        timer_lbl.config(text="Break", fg=PINK)
        count_down(2) # short break
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # format time
    # past : #count_formatted = f"{count//60}:{count%60}"
    minutes = count // 60
    seconds = count % 60
    if minutes < 10:
        minutes = f"0{minutes}"
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global counting
        counting = window.after(1000, count_down, count-1)
    else:
        # i enter here when i finish a session
        start_timer() # to automatically switch sessions
        global checks 
        checks = reps // 2
        checkmark.config(text="✔"*checks)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro App")
window.config(padx=50, pady=50, bg=YELLOW)

timer_lbl = tkinter.Label(text="Timer", font=FONT, foreground=GREEN, background=YELLOW, highlightthickness=0)
timer_lbl.config(padx=10, pady=10)
timer_lbl.grid(row=0, column=1)

canvas = tkinter.Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
ph_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=ph_img)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=FONT)
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start", font=(FONT_NAME, 14))
start_button.config(padx=10, pady=10, command=start_timer)
start_button.grid(row=2, column=0)

checkmark = tkinter.Label(fg=RED, font=(FONT_NAME, 16), bg= YELLOW,  highlightthickness=0)
checkmark.config(padx=10, pady=10)
checkmark.grid(row=2, column=1)

reset_button = tkinter.Button(text="Reset", font=(FONT_NAME, 14))
reset_button.config(command=reset_timer, padx=10, pady=10)
reset_button.grid(row=2, column=2)

# calling functions
window.mainloop()