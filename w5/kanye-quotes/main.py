import requests, tkinter


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    canvas.itemconfig(quote_text, text=response.json()["quote"])

window = tkinter.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=300, height=414)
background_img = tkinter.PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = tkinter.PhotoImage(file="kanye.png")
kanye_button = tkinter.Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()