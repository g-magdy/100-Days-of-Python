import tkinter

# WINDOW
window = tkinter.Tk()
window.minsize(400, 400)
window.title("Miles to kilometers Calculator")

# LABEL 1 
lab = tkinter.Label(text="Enter miles, see kilomters")
lab.pack()

# ENTRY FIELD
prompt = tkinter.Entry()
prompt.config(font=("Courier", 18))
prompt.pack()
prompt.focus()

def convert():
    mile = float(prompt.get())
    km = mile * 1.609344
    out.config(text=f"{mile} miles= {round(km, 3)} kms")

# BUTTON
button = tkinter.Button(text="Convert!")
button.config(command=convert)
button.pack()


# OUTPUT LABEL
out = tkinter.Label(text="0")
out.config(font=("Courier", 20))
out.pack()

window.mainloop()