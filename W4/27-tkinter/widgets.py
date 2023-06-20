import tkinter

'''
Space management - place managers in tkinter are pack - place - grid
'''
# WINDOW
window = tkinter.Tk()
window.title("My Game")
window.minsize(500, 500)

window.config(padx=20, pady=20)

# LABEL
label = tkinter.Label(text="Hello Label", padx=10, pady=10)
label.grid(column=0, row=0)

# ENTRY
prompt = tkinter.Entry(width=12)
prompt.focus()
prompt.grid(column=3, row=2)

# BUTTON
button = tkinter.Button(text="Button A", padx=10, pady=10)
button.grid(column=1, row=1)

# BUTTON 2
button2 = tkinter.Button(text="Button B", padx=10, pady=10)
button2.grid(column=2, row=0)



# # TEXT
# txt = tkinter.Text(height=20, width=30)
# txt.focus()
# txt.pack()

# RADIOBUTTON
# SCALE
# CHECKBUTTON
# SPINBOX
# LISTBOX

window.mainloop()