import tkinter

FONT = ("Courier", 16)
PADDING = 6

def convert():
    miles = float(prompt.get())
    result.config(text=f"{round(miles*1.609, 3)}")

# i'd use 6 objects

# WINDOW 
window = tkinter.Tk()
window.title("Miles to Km converter")
window.config(padx=PADDING*2, pady=PADDING*2)

# ENTRY
prompt = tkinter.Entry(width=PADDING, font=FONT)
prompt.grid(row=0, column=1)
prompt.focus()

l1 = tkinter.Label(text="Miles", font=FONT, padx=PADDING, pady=PADDING)
l1.grid(row=0, column=2)

l2 = tkinter.Label(text="is equal to", font=FONT, padx=PADDING, pady=PADDING)
l2.grid(row=1, column=0)

result = tkinter.Label(text="0", font=FONT, padx=PADDING, pady=PADDING)
result.grid(row=1, column=1)

l3 = tkinter.Label(text="Km", font=FONT, padx=PADDING, pady=PADDING)
l3.grid(row=1, column=2)


# BUTTON
convert_button = tkinter.Button(text="Calculate", command=convert, font=FONT)
convert_button.grid(row=2, column=1)
convert_button.config(padx=PADDING, pady=PADDING)

window.mainloop()