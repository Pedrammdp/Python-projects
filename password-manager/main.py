from tkinter import *
from tkinter import messagebox
import random
import string
#  PASSWORD GENERATOR  #
def generate_password():
    letters = string.ascii_letters
    numbers =  string.digits
    symbols = string.punctuation

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0, password)
#  SAVE PASSWORD  #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, 
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\n\nSave?"
        )

        if is_ok:
            with open("data.csv", "a") as data_file:
                data_file.write(f"{website}, {email}, {password}\n")
            
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file="2. password-manager-start/logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(row= 0, column=1)

# Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
password_label = Label(text="password")
password_label.grid(row=3,column=0)

#Entry
website_entry =Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "pedimdp@yahoo.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Button
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width =36, command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
