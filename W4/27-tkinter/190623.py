import tkinter

# windows in tkinter are equivalent to screens in turtle

window = tkinter.Tk()
window.title("First GUI program")
window.minsize(width=500, height=500)

label = tkinter.Label(text="What is this ?", font=("Arial", 24, "bold"))
label.pack() #to display the label in a geometric way

# always at the end
window.mainloop()