from tkinter import *

root = Tk()
root.title("Radiobuttons")

SelectOption = [
    ("selection1", "Hyundai"),
    ("selection2", "BMW"),
    ("selection3", "Volvo"),
    ("selection4", "Ford")
]

choices = StringVar()
choices.set("selection1")

for text, mode in SelectOption:
    Radiobutton(root, text=text, variable=choices, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

myButton = Button(root, text="Test this out!", command=lambda: clicked(choices.get()))
myButton.pack()

root.mainloop()