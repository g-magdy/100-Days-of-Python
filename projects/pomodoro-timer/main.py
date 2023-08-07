import tkinter
from playsound import playsound
# ADD 
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ("Chewy", 36, "normal")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks = ""
recurse = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global recurse
    if recurse:
        window.after_cancel(recurse)
        canvas.itemconfig(timer_text, text="00:00")
        global reps,checkmarks
        reps= 0
        checkmarks = 0
        checkmaks_label.config(text="")
        timer_title.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def begin_countdown():
    work_sec = 10
    short_break_sec = 5
    long_break_sec = 7
    # work_sec = WORK_MIN * 60
    # short_break_sec = SHORT_BREAK_MIN * 60
    # long_break_sec = LONG_BREAK_MIN * 60
    global reps
    reps += 1
    # long break
    if reps % 8 == 0:
        timer_title.config(text="Long Break")
        playsound("start-long-break.wav")
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_title.config(text="Short Break")
        playsound("start-short-break.wav")
        checkmaks_label.config(text="✔" * (reps // 2))
        count_down(short_break_sec)
    else:
        timer_title.config(text="Work")
        playsound("start-work.wav")
        count_down(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(seconds):
    min = seconds // 60
    min = f"0{min}" if min < 10 else min
    sec = seconds % 60
    sec = f"0{sec}" if sec < 10 else sec
    time_formatted = f"{min}:{sec}"
    canvas.itemconfig(timer_text, text=time_formatted)
    if seconds > 0:
        global recurse
        recurse = window.after(1000, count_down, seconds-1)
    else:
        begin_countdown()
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", font=FONT, fill="white")

timer_title = tkinter.Label(text="Timer", fg=GREEN, font=FONT, bg=YELLOW, highlightthickness=0)

start_button = tkinter.Button(text="Start", bg=GREEN, fg=YELLOW, font=("Chewy", 20), command=begin_countdown)

reset_button = tkinter.Button(text="Reset", bg=GREEN, fg=YELLOW, font=("Chewy", 20), command=reset_timer)

checkmaks_label = tkinter.Label(text=checkmarks, bg=YELLOW, fg=GREEN, font=("Chewy", 20))

timer_title.grid(column=1, row=0)
canvas.grid(column=1, row=1)
checkmaks_label.grid(column=1, row=3)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)

window.mainloop()
