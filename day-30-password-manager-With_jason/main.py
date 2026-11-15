from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(2, 4)

    #list comprehnsion used in the same code as day 5
     #[new_item for item in range]

    password_letters =[random.choice(letters) for _ in range(nr_letters)]
    password_symbols =[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers =[random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    #  OR
    password = "".join(password_list) #using join
    password_entry.insert(0, password)

    pyperclip.copy(password) #without ctrl+v the password is automatically copied
    print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #



def save():

        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        new_data ={
            website:
                {
                    "email": email,
                 "password": password,
                }
        }



        if website == "" or email == "" or password == "":
           messagebox.showinfo(title="Oops", message="Please dont leave any field empty!")
        else:

        #changing file format to json in write mode from txt append
            try:
                with open("data.json", "r") as data_file:
                    # reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                #if file not found make another file in write mode
                with open("data.json", "w") as data_file:
                    json.dumps(new_data, data_file, indent=4)
            else:
                #updating old data with new data
                data.update(new_data)

                with open('data.json', 'w') as data_file:
                    #saving updated data
                    json.dump(data, data_file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")

# ---------------------------- UI SETUP ------------------------------- #
# Canvas
window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60)

canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(window, text="Website:", font=("Times New Roman", 10))
website_label.grid(row=1, column=0, sticky="e")

email_label = Label(window, text="Email/Username:", font=("Times New Roman", 10))
email_label.grid(row=2, column=0, sticky="e")

password_label = Label(window, text="Password:", font=("Times New Roman", 10))
password_label.grid(row=3, column=0, sticky="e")

# Entries
website_entry = Entry(width=33)
website_entry.grid(row=1, column=1, sticky="w")

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2, sticky="w")
email_entry.insert(0, "salehamallick1622@gmail.com")

password_entry = Entry(width=33)
password_entry.grid(row=3, column=1, sticky="w")

# Buttons
search_button = Button(text="Search", width=13,command=find_password)
search_button.grid(row=1, column=2, sticky="w")

generate_password_button = Button(
    window,
    text="Generate Password",
    command=generate_password
)
generate_password_button.grid(row=3, column=2, sticky="w")

add_button = Button(
    window,
    width=36,
    text="Add",
    command=save
)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")
# window = Tk()
# window.title("Password Manager")
# window.config(padx=60, pady=60)
#
# #canvas - the picture that we are adding
# canvas = Canvas(window, width=200, height=200)
# logo = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=logo)
# canvas.grid(row=0, column=1)
#
# #label
# website_label = Label( text="Website:",font=("Times New Roman", 10))
# website_label.grid(row=1, column=0)
#
# email_label = Label( text="Email/Username:",font=("Times New Roman", 10))
# email_label.grid(row=2, column=0)
#
# password_label = Label( text="Password:",font=("Times New Roman", 10))
# password_label.grid(row=3, column=0)
#
#
#
# #entry
# website_entry = Entry( width=21)
# website_entry.grid(row=1, column=1,columnspan=2)
#
# email_entry = Entry( width=35)
# email_entry.grid(row=2, column=1,columnspan=2,sticky="w")
# email_entry.insert(0,"salehamallick1622@gmail.com")
# password_entry = Entry( width=17)
# password_entry.grid(row=3, column=1)
#
# #button
# search_button = Button( text=" Search " ,width=10)
# search_button.grid(row=1, column=2)
#
# generate_password_button = Button(window, text="Generate Password",command=generate_password)
# generate_password_button.grid(row=3, column=2)
#
# add_button = Button(window,width=36, text="Add",command=save)
# add_button.grid(row=4, column=1,columnspan=2)



window.mainloop()