import pyperclip
import json
import customtkinter

from numpy import random
from tkinter import *
from tkinter import messagebox
from PIL import Image
from config import FONT_TYPE, FONT_SIZE, SET_DEFAULT_EMAIL_OR_USERNAME, MIN_LETTERS, MAX_LETTERS, MIN_SYMBOLS, MAX_SYMBOLS, MIN_NUMBERS, MAX_NUMBERS
from datetime import date

DATE = date.today().strftime("%Y-%b-%d")


# ---------------------------- SEARCH ------------------------------- #


def search():
    def display_data(website, data):
        top = Toplevel()
        top.title(website)
        top.minsize(550, 250)
        top.maxsize(550, 250)
        top.iconbitmap('images/logo.ico')

        text = Text(top, height=10, width=50, font=(FONT, 16), pady=30, state="normal")
        text.pack()
        
        text.tag_configure("center", justify="center")

        text.insert(END, f"Created on {data['date']}\n\n")
        text.insert(END, f"Email: {data['email']}\n\n")
        text.insert(END, f"Password: {data['password']}\n\n")
               
        text.tag_add("center", "1.0", "end")
        text.configure(state="disabled")
        
    website = website_entry.get()
    try:
        with open("data.json", "r") as data:
            data_from_file = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="FileNotFoundError",
                            message="There is no such file, please add an entry first")
    else:
        if website in data_from_file:
            display_data(website, data_from_file[website])
        else:
            messagebox.showinfo(
                title=website, message="No entry with this name.")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def random_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(int(MIN_LETTERS), int(MAX_LETTERS))
    nr_symbols = random.randint(int(MIN_SYMBOLS), int(MAX_SYMBOLS))
    nr_numbers = random.randint(int(MIN_NUMBERS), int(MAX_NUMBERS))

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list.extend([random.choice(symbols) for _ in range(nr_symbols)])
    password_list.extend([random.choice(numbers) for _ in range(nr_numbers)])

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    # Instantly copies to the clipboard:
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    def save_to_file():
        # --------- TXT version --------- #
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password} | {DATE}\n")

        # --------- JSON version --------- #
        try:
            with open("data.json", "r") as data:
                data_from_file = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            data_from_file.update(new_data)
            with open("data.json", "w") as data:
                json.dump(data_from_file, data, indent=4)
            pyperclip.copy(password)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            update_entries_number_label()
 
            
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
   
    new_data = {website: {"email": email, "password": password, "date": DATE}}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty field!", message="No field can be empty!")
    else:
        try:
            with open("data.json", "r") as data:
                data_from_file = json.load(data)
        except FileNotFoundError:
            save_to_file()
        else:
            if website in data_from_file:
                overwrite = messagebox.askokcancel(title=website, message=f"{website} already exist and created on {data_from_file[website]['date']} \n\nOverwrite it?")
                if overwrite:
                    save_to_file()
                
            else:
                confirm = messagebox.askokcancel(title=website, message=f"These are the details entered for {website} \n\nEmail:  {email} \n\nPassword:  {password} \n\nIs everything right? \n\nTip: Once accepted, the password is stored in the clipboard and is ready for further use! 😉")
                if confirm:
                    save_to_file()                                


# ---------------------------- LENGTH CHECKER ------------------------------- #


def length_checker():
    try:
        with open("data.json") as data:
            entries_number = json.load(data)
        return len(entries_number)
    except FileNotFoundError:
        return 0
    
def update_entries_number_label():
    with open("data.json") as data:
        entries_number = json.load(data)
    entries_number_label.configure(text=f"The total number of entries is: {len(entries_number)}")


# ---------------------------- UI SETUP ------------------------------- #
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

window = customtkinter.CTk()

window.minsize(1000, 600)
window.maxsize(1000, 600)
window.title("Pocket Password Generator")

window.iconbitmap('images/logo.ico')
window.config(padx=60, pady=70)


# ----- FONT LOAD ----- #
FONT = customtkinter.CTkFont(family=FONT_TYPE, size=FONT_SIZE)


# ----- LOAD IMAGES ----- #
add_folder_image = customtkinter.CTkImage(dark_image=Image.open("images/diskette.png"), size=(20, 20))
add_quit_image = customtkinter.CTkImage(dark_image=Image.open("images/logout.png"), size=(20, 20))
add_search_image = customtkinter.CTkImage(dark_image=Image.open("images/magnifying-glass.png"), size=(20, 20))


# 0 Column
website_label = customtkinter.CTkLabel(master=window, text="Website:", font=FONT)
website_label.grid(column=0, row=1)

email_label = customtkinter.CTkLabel(master=window, text="Email/Username:", font=FONT)
email_label.grid(column=0, row=2)

password_label = customtkinter.CTkLabel(master=window, text="Password:", font=FONT)
password_label.grid(column=0, row=3)

window.grid_rowconfigure(6, minsize=60)

entries_number_label = customtkinter.CTkLabel(master=window, text=f"The total number of entries is: {length_checker()}", font=FONT)
entries_number_label.grid(column=0, row=7, columnspan=2)


# 1 Column
website_entry = customtkinter.CTkEntry(master=window, placeholder_text="page name...", width=300, height=35, border_width=2, corner_radius=10, font=(FONT, 22))
website_entry.grid(column=1, row=1, padx=20, pady=20)
website_entry.focus()

email_entry = customtkinter.CTkEntry(master=window, placeholder_text="email...", width=300, height=35, border_width=2, corner_radius=10, font=(FONT, 22))
email_entry.insert(0, SET_DEFAULT_EMAIL_OR_USERNAME)
email_entry.grid(column=1, row=2, padx=20, pady=20)

password_entry = customtkinter.CTkEntry(master=window, placeholder_text="password...", width=300, height=35, border_width=2, corner_radius=10, font=(FONT, 22))
password_entry.grid(column=1, row=3, padx=20, pady=20)

add_button = customtkinter.CTkButton(master=window, image=add_folder_image, text="Save", width=150, height=35, command=save, font=(FONT, 22), fg_color="#03C988", text_color="#03001C", compound="right", hover_color="#51c26a")
add_button.grid(column=1, row=4, padx=20, pady=40)


# 2 Column
search_button = customtkinter.CTkButton(master=window, text="Search", image=add_search_image, width=190, height=35, command=search, font=(FONT, 22), fg_color="#1C82AD", compound="right")
search_button.grid(column=2, row=1, padx=20, pady=20)

random_password_button = customtkinter.CTkButton(master=window, text="Generate Password", width=190, height=35, command=random_password, font=(FONT, 22), fg_color="#1C82AD", anchor="center")
random_password_button.grid(column=2, row=3, padx=20, pady=20)

quit_button = customtkinter.CTkButton(master=window, text="Quit", image=add_quit_image, width=150, height=35, command=window.destroy, font=(FONT, 22), fg_color="#9c1919", text_color="#03001C", compound="right", hover_color="#bd1515")
quit_button.grid(column=2, row=7, padx=20, pady=20)



window.mainloop()
