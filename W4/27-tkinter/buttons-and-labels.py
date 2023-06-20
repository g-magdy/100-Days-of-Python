import tkinter

# SCREEN - WINDOW
window = tkinter.Tk()
window.title("learn")
# window.config(bg="black")
window.minsize(width=400, height=400) # limit the size - can't minimize more

# LABEL
mylabel = tkinter.Label(text="This is a label", font=("Courier", 24, "bold"))
mylabel.pack()
 
def button_clicked():
    s = prompt.get()
    mylabel.config(text=s)

# BUTTON
mybutton = tkinter.Button(text="click me")
mybutton.pack()
mybutton.config(command=button_clicked) # don't put the parentheses

# HANDLNG INPUT 

prompt = tkinter.Entry()
prompt.config(font=("Courier", 18, "normal"), width=5)
prompt.pack()
prompt.focus()



window.mainloop()