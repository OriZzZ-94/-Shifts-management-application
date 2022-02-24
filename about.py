from tkinter import *

def about():
    aboutwin = Toplevel()
    aboutwin.title("About Schedule Generator")
    aboutwin.geometry('200x200')
    about_label1 = Label(aboutwin, text = "Schedule generator was created by:", anchor = 'center')
    about_label2 = Label(aboutwin, text = "Matan Cohen", anchor = 'center')
    about_label3 = Label(aboutwin, text="Ethan Attali", anchor='center')
    about_label4 = Label(aboutwin, text="Ori Ashkenzi", anchor='center')
    about_label1.pack()
    about_label2.pack()
    about_label3.pack()
    about_label4.pack()
