import tkinter, csv, random, pyperclip, json
from tkinter import messagebox
from string import digits, ascii_lowercase, ascii_uppercase
# ---------------------------- CONSTANTS ------------------------------- #
# TODO: change this email :)
DEFAULT_EMAIL = "jerry@gmail.com"
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
    website = website_in.get().lower()
    email = email_in.get()
    password = pwd_in.get()
    if "" in [website, email, password]:
        messagebox.showwarning(title="Empty fields warning",
                             message="Please fill out all fields")
        return
    
    # check if the website name already exists!
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                messagebox.showwarning(title="Could not add website", message="Website already exists!")
                return
    except FileNotFoundError:
        messagebox.showerror("data.json was not found")
    
    confirmation = messagebox.askokcancel(title=f"{website.capitalize()}",
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
                                "Your password was copied to the clipboard too!")

# ---------------------------- FIND PREVIOUSLY SAVED DATA ------------------------------- #
def find_website():
    website = website_in.get().lower()
    if website != "":
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                answer = messagebox.askyesno(
                    title=website.capitalize(),
                    message=f"email : {data[website]['email']}\n"
                    f"password : {data[website]['password']}\n"
                    "Do you want me to copy the password to the clipboard ?"
                )
                if answer:
                    pyperclip.copy(data[website]["password"])
                    messagebox.showinfo(title="success", message="password was copied!")
        except FileNotFoundError:
            messagebox.showerror(title="Could not search", message="data.json was not found")
        except KeyError as k:
            messagebox.showerror(title="Key does not exist", message=f"{k} does not exist in data.json")
    else:
        messagebox.showwarning(title="Could not search", message="Website name cannot be empty")
    
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# creating widgets
canvas = tkinter.Canvas(height=200, width=200)
img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
website_label = tkinter.Label(text="Website: ")
search_button = tkinter.Button(text="Search", width=10, command=find_website)
website_in = tkinter.Entry(width=35)
website_in.focus()
email_label = tkinter.Label(text="Email/Username: ")
pwd_label = tkinter.Label(text="Password: ")
email_in = tkinter.Entry(width=35)
email_in.insert(0, DEFAULT_EMAIL)
pwd_in = tkinter.Entry(width=35)
gen_pwd_button = tkinter.Button(text="Generate Password", command=generate_pwd)
add_button = tkinter.Button(text="Add", width=36, command=register)

# placement
canvas.grid(row=0, column=1)

website_label.grid(row=1, column=0)
website_in.grid(row=1, column=1, columnspan=2)
search_button.grid(row=1, column=3)

email_label.grid(row=2, column=0)
email_in.grid(row=2, column=1, columnspan=2)

pwd_label.grid(row=3, column=0)
pwd_in.grid(row=3, column=1)
gen_pwd_button.grid(row=3, column=3)

add_button.grid(row=4, column=1)

window.mainloop()
