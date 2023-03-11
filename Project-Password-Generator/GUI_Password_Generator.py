# from msilib.schema import CheckBox
import random
from tkinter import *
from tkinter import ttk
import tkinter
import string


# creating a window.
window = Tk()

# providing the title of the window.
window.title("Password Generator")


# setting the size of the window.
window.geometry("300x400")

# adding a label
Label(window, font=('bold', 18), text='Password Generator').pack()


# function to generate random password

def getLength():
    # getLength function will call the passwordGeneration function
    characterList = ""
    characterList += string.ascii_lowercase

    if pass_cap.get() == 1:
        characterList += string.ascii_uppercase
    if pass_num.get() == 1:
        characterList += string.digits
    if pass_spl.get() == 1:
        characterList += string.punctuation

    # get the password length from the text box
    pass_length = int(length_entry.get())

    password = []
    for i in range(pass_length):
        randomchar = random.choice(characterList)
        password.append(randomchar)

    # display the generated password
    password_label.config(text="".join(password))


# GUI PART
# creating buttons
Button(window, text='Generate Password', font=('normal', 10),
       bg='lightblue', command=getLength).place(x=80, y=150)

# creating checkboxes
pass_cap = tkinter.IntVar()
pass_num = tkinter.IntVar()
pass_spl = tkinter.IntVar()

Checkbutton(text='Include CAPS', onvalue=1, offvalue=0,
            variable=pass_cap).place(x=90, y=200)
Checkbutton(text='Include Numbers', onvalue=1, offvalue=0,
            variable=pass_num).place(x=90, y=220)
Checkbutton(text='Include Special Characters', onvalue=1, offvalue=0,
            variable=pass_spl).place(x=90, y=240)

# adding a text box for entering password length
length_label = Label(window, text="Enter Password Length")
length_label.place(x=20, y=100)
length_entry = Entry(window)
length_entry.place(x=150, y=100)

# adding a label for displaying the generated password
password_label = Label(window, font=('bold', 25))
password_label.place(x=45, y=275)

window.mainloop()
