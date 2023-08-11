import tkinter, csv, random, pyperclip, json
from tkinter import messagebox
from string import digits, ascii_lowercase, ascii_uppercase
#Potential features
# 1. check for repeated entries of a website
# 2. validate wbsite name
# #
# ---------------------------- CONSTANTS ------------------------------- #
DEFAULT_EMAIL = "georgetwafik09@gmail.com"
SYMBOLS =['!', '#', '$', '%', '&', '*', '(', ')', '+']
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    password = []
    for lst in [digits, ascii_lowercase, ascii_uppercase, SYMBOLS]:
        password += random.choices(lst, k=random.randint(3, 6))
    random.shuffle(password)
    password = "".join(password)
    
    if pwd_in.get() != "":
        answer = messagebox.askyesno(title="Password",
                               message="The password field is not empty\n"
                               "Are you sure you want to delete it\n"
                               "And replace it with a generated one")
        if answer is False:
            return
    
    pwd_in.delete(0, tkinter.END)
    pwd_in.insert(0, password)
            
# ---------------------------- SAVE PASSWORD ------------------------------- #
def register():
    website = website_in.get()
    email = email_in.get()
    password = pwd_in.get()
    if "" in [website, email, password]:
        messagebox.showwarning(title="Empty fields warning",
                             message="Please fill out all fields")
        return
    
    confirmation = messagebox.askokcancel(title=f"{website}",
                                   message=f"Email: {email}\nPassword: {password}\nSave this ?")
    if confirmation:
        new_data = {
            website: {
                "email":email,
                "password":password
            }
        }
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_in.delete(0, tkinter.END)
            pwd_in.delete(0, tkinter.END)
            pyperclip.copy(password)
            messagebox.showinfo(title="Done!", 
                                message="Your data was saved in data.json\n"
                                "Your password was compied to the clipboard too!")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(height=200, width=200)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
website_label = tkinter.Label(text="Website: ")
email_label = tkinter.Label(text="Email/Username: ")
pwd_label = tkinter.Label(text="Password: ")
website_in = tkinter.Entry(width=35)
website_in.focus()
email_in = tkinter.Entry(width=35)
email_in.insert(0, DEFAULT_EMAIL)
pwd_in = tkinter.Entry(width=35)
gen_pwd_button = tkinter.Button(text="Generate Password", command=generate_pwd)
add_button = tkinter.Button(text="Add", width=36, command=register)

# placement
canvas.grid(row=0, column=1)

website_label.grid(row=1, column=0)
website_in.grid(row=1, column=1, columnspan=2)

email_label.grid(row=2, column=0)
email_in.grid(row=2, column=1, columnspan=2)

pwd_label.grid(row=3, column=0)
pwd_in.grid(row=3, column=1)
gen_pwd_button.grid(row=3, column=3)

add_button.grid(row=4, column=1)

window.mainloop()
