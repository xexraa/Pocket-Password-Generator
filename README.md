# Pocket Password Generator

## The application has two possibilities of use

The exe file is a ready-to-use product, just download and install it on your computer to enjoy the program, or alternatively, you can download the classic Python scripts and use them in your interpreter.
More information below.

## Brief description of the program:

Do you often struggle with remembering various passwords, or find them scattered across different files? This program can help you keep your files organized. Pocket Password Generator is a small program designed for everyday use, hence the name "Pocket." It allows you to save your passwords to files, and includes options to search for previously saved passwords as well as create completely random and strong passwords. The user can also adjust the length and composition of the generated password. A full program description can be found below.

# Installation options

## First "exe"

- Download the file "PocketPasswordGenerator_WINDOWS_1.5_setup.exe"
- During installation, you will be prompted for standard options like creating a shortcut and selecting a save path.
- After installation, navigate to the main folder (usually located at "C:\Program Files (x86)\Pocket Password Generator"), and open the "config.ini" file.
- In this file, you can set the size of the generated password and specify a default email/username, so that it will be pre-filled when you open the program.
- Enter your most commonly used email address and try to save the file. If you encounter any problems with saving, you may need to grant permissions to users by right-clicking on the main program folder, selecting "Properties," then "Security," and finally "Edit." From there, you can add users and grant them full permissions.
- Once you have made the necessary changes, try again to save the file. If successful, you can fully use the program.
- Note that granting permissions is necessary because without them, the program will not be able to create database files.

## Second "scripts"

To use the Python scripts, simply download them. The "requirements.txt" file contains all the necessary libraries. You can adjust the parameters in the "config.ini" file.

# Full program description

During the first use, the program looks like this: 
![first_use](https://user-images.githubusercontent.com/121942715/230446485-cda500a0-904c-49a6-b721-5afeb834e2ea.png)

- The "Search" button searches by "Website".
- The "Generate Password" button generates a random password.
- The "Save" button saves to two files: "data.txt", which is for those who prefer to have their passwords saved in a text file. Passwords are saved in a readable and user-friendly format. It also simultaneously creates the "data.json" file, which is the database of our program that it interacts with.
- The "Quit" button allows you to exit the program.

## Search option

Next, we set a default name and saved the "Example" website and password. When we click the "Search" button, a user-friendly window pops up:
![search](https://user-images.githubusercontent.com/121942715/230447852-20b75d2e-9bba-4275-8a33-2c8de600c2b2.png)

This window allows us to easily select and copy the password for further use. Additionally, it provides information about when the password was created.

## Save option

When we add a new entry, a window will pop up allowing us to double-check for errors. After pressing "OK," the entry will be added to our database. Additionally, whether the password is randomly generated or manually entered, it is immediately added to our computer's clipboard so that we can easily use it when creating an account on a website.
![add_new](https://user-images.githubusercontent.com/121942715/230449502-dd7881c9-750e-4609-8e3f-a54092e1325c.png)

## Generate password option

In the config.ini file, we have the ability to customize the password to our needs, by default, it has a length of 12 to 18 characters.

![config](https://user-images.githubusercontent.com/121942715/230450919-916e6cf2-c633-4269-80dd-00808714350f.png)

## Footer

Below that, there is a purely statistical information about how many passwords we have already saved, and a Quit button that allows us to close the program.

## In addition

- The program adds the current date to every saved password.
- The program detects if we already have a record for a given website and asks if we want to overwrite the password.
- The program does not allow saving when any field is empty.


## What sources did I use?

**Python:**

- Pillow
- customtkinter
- pyperclip
- numpy


**Programs:**

- GIT
- VSC
