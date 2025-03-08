import tkinter
from tkinter import ttk
import random
import time

NUM_WORDS = 10
TEXT_FILE = "new_text.txt" 

def refresh_text(number_of_sentences):
    """Loads random sample text from the file and updates the UI."""
    with open(TEXT_FILE, "r") as texts_file:
        words = texts_file.read().lower().split()
        chosen_words = random.sample(words, NUM_WORDS)
        text = " ".join(chosen_words)
        sample_text.set(text)
        
    text_box.config(state=tkinter.NORMAL)
    timer_seconds.set("0 seconds")
    text_box.delete("1.0", "end")
    speed_label.pack_forget()
    accuracy_label.pack_forget()
    time_label.pack_forget()
    text_box.focus_set()
    text_box.bind("<Key>", start_timer)
    text_box.bind("<KeyRelease>", lambda event: check_auto_submit())  # Auto-submit when typed text reaches target length



def delete_previous_word(event):
    """Allows Ctrl+Backspace to delete the last word."""
    cursor_position = text_box.index(tkinter.INSERT)
    if cursor_position == "1.0":
        return "break"

    # Find the start of the previous word
    previous_word_start = text_box.search(r'\s', cursor_position, backwards=True, regexp=True)
    if not previous_word_start:
        previous_word_start = "1.0"

    # Delete the word
    text_box.delete(previous_word_start, cursor_position)
    return "break"


def start_timer(event):
    """Starts the timer when the user types the first key."""
    global timer_is_running, start_time
    if not timer_is_running:
        start_time = time.time()
        timer_is_running = True
        update_timer()

    check_auto_submit()


def update_timer():
    """Updates the timer every second."""
    if timer_is_running:
        elapsed_time = round(time.time() - start_time, 2)
        timer_seconds.set(f"{elapsed_time} seconds")
        root.after(100, update_timer)


def calculate_results():
    """Calculates typing speed (WPM) and accuracy."""
    global timer_is_running, start_time, end_time

    if not timer_is_running:
        return

    end_time = time.time()
    timer_is_running = False

    # Get user input
    user_text = text_box.get("1.0", "end").strip()
    target_text = sample_text.get().strip()

    # Calculate Words Per Minute (WPM)
    elapsed_time = end_time - start_time
    word_count = len(user_text.split())
    wpm = round((word_count / elapsed_time) * 60) if elapsed_time > 0 else 0

    # Calculate accuracy
    correct_chars = sum(1 for a, b in zip(user_text, target_text) if a == b)
    accuracy = round((correct_chars / len(target_text)) * 100) if target_text else 0

    # Update UI
    speed_label.config(text=f"Speed: {wpm} WPM")
    speed_label.pack(pady=5)
    accuracy_label.config(text=f"Accuracy: {accuracy}%")
    accuracy_label.pack(pady=5)
    time_label.config(text=f"Time Taken: {round(elapsed_time, 2)} seconds")
    time_label.pack(pady=5)
    text_box.config(state=tkinter.DISABLED)
    timer_label.pack_forget()
    
    help_text.pack_forget()


def check_auto_submit():
    """Automatically submits when the user types all characters."""
    global timer_is_running
    
    if timer_is_running == False:
        return
    
    user_text = text_box.get("1.0", "end").strip()
    target_text = sample_text.get().strip()

    if len(user_text) == len(target_text):
        text_box.unbind("<Key>")
        text_box.unbind("<KeyRelease>")
        calculate_results()


def reset_test():
    """Resets the typing test."""
    global timer_is_running, start_time, end_time
    timer_is_running = False
    start_time = None
    end_time = None
    timer_seconds.set("0 seconds")
    text_box.delete("1.0", "end")
    speed_label.config(text="Speed: 0 WPM")
    accuracy_label.config(text="Accuracy: 0%")
    time_label.config(text="Time Taken: 0 seconds")


# Root window
root = tkinter.Tk()
root.title("Typing Speed Test")
root.geometry("1280x720")
root.configure(bg="#3498db")

# Title Label
top_label = tkinter.Label(root, text="Typing Speed Test", font=("Arial", 24), bg="#3498db", fg="#ffffff")
top_label.pack(pady=20)

# StringVar for sample text
sample_text = tkinter.StringVar()
timer_seconds = tkinter.StringVar()
timer_seconds.set("0 seconds")

# Sample Text Label
sample_text_label = tkinter.Label(root, textvariable=sample_text, font=("Arial", 14), wraplength=800, bg="#3498db", fg="#ffffff")
sample_text_label.pack(pady=20)

# Refresh Text Button
refresh_button = tkinter.Button(root, text="Refresh", font=("Arial", 14), bg="#ffffff", fg="#3498db", command=lambda: refresh_text(NUM_WORDS))
refresh_button.pack(pady=10)

# Text Box for Typing
text_box = tkinter.Text(root, height=10, width=70, font=("Arial", 14))
text_box.pack(pady=10)
text_box.bind("<Control-BackSpace>", delete_previous_word)
text_box.focus_set()
text_box.bind("<Key>", start_timer)
text_box.bind("<KeyRelease>", lambda event: check_auto_submit())  # Auto-submit when typed text reaches target length

# Timer Label
timer_label = tkinter.Label(root, textvariable=timer_seconds, font=("Arial", 14), bg="#3498db", fg="#ffffff")
timer_label.pack(pady=5)

# help text
help_text = tkinter.Label(root, text="the time starts when you type the first character\nAnd it ends when typing a number of characters = given characters", font=("Arial", 12), bg="#3498db", fg="#ffffff")
help_text.pack(pady=5)

# Results Section
speed_label = tkinter.Label(root, text="Speed: 0 WPM", font=("Arial", 14), bg="#3498db", fg="#ffffff")

accuracy_label = tkinter.Label(root, text="Accuracy: 0%", font=("Arial", 14), bg="#3498db", fg="#ffffff")

time_label = tkinter.Label(root, text="Time Taken: 0 seconds", font=("Arial", 14), bg="#3498db", fg="#ffffff")

# Global variables
timer_is_running = False
start_time = None
end_time = None

# Load first text
refresh_text(NUM_WORDS)

# Run the app
root.update_idletasks()  # Updates layout
root.geometry("")  # Automatically fits content
root.mainloop()
