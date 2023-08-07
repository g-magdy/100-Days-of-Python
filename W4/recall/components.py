import tkinter

def main():
    window = tkinter.Tk()
    window.minsize(height=500, width=500)
    window.title("hello")

    heading = tkinter.Label(text="Hello", font=("Calibri", 22, "bold"))
    
    button = tkinter.Button(text="Click me!",
                            command=lambda : heading.config(text="clicked"))
    
    submit = tkinter.Button(text="Print", command=lambda: print(entry.get()))
    
    entry = tkinter.Entry()
    
    heading.pack()
    entry.pack()
    button.pack()
    submit.pack()
    window.mainloop()


main()