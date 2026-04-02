# Open UI library
from tkinter import *
from tkinter import messagebox

# Tk() = new window.
root = Tk()
root.title("Message practice")
root.geometry("400x400")

# Function button pressing handler
def IClicked():
    # Write text lable which 
    buttonClickLabel=Label(root, text="Button pressed")
    buttonClickLabel.pack()

# Disabled button
disabledButton = Button(root, text="Press button", state=DISABLED)

# Active button
activeButton = Button(root, text="Press button", padx=50, pady=50, command=IClicked, fg="red")
activeButton.pack()

# Messagebox
def popup():
    respone = messagebox.askyesno("Messagebox wants to say: ", "Here I am")
    # If user press Yes:
    if respone == 1:
        Label(root, text="You pressed Yes button!").pack()
    # If user press No:
    else:
        Label(root, text="You pressed No button!").pack()

# New window
def open():
    top = Toplevel()
    top.title("New window")
    closeWindowButton = Button(top, text="Close window", command=top.destroy).pack()

# Dropdown
options=[
    "First",
    "2nd",
    "3rd",
    "4th",
    "5th"
]

selectItem = StringVar()
selectItem.set(options[0])

def show():
    myLabel=Label(root, text=selectItem.get()).pack()

drop = OptionMenu(root, selectItem, *options)
drop.pack()

myButton = Button(root, text="Select here", command=show).pack()

openWindowButton = Button(root, text="Open new window", command=open).pack()
Button(root, text="CLICKMEE", command=popup).pack()
root.mainloop()