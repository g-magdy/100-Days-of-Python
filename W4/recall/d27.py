import tkinter

# main window
window = tkinter.Tk()
window.title("Recall Tkinter")
window.minsize(width=500, height=500)

# create component
font1 = ("Calibri", 22, "italic")
top = tkinter.Label(text="Top", font=font1)
top.pack(side="top")
bottom = tkinter.Label(text="Bottom", font=font1)
bottom.pack(side="bottom")
left = tkinter.Label(text="Left", font=font1)
left.pack(side="left")
right = tkinter.Label(text="Right", font=font1)
right.pack(side="right")
center = tkinter.Label(text="center", font=font1)
center.pack(expand=True)



# last line of the program
window.mainloop()
