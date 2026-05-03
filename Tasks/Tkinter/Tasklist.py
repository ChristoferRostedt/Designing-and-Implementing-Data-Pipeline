import sqlite3
import tkinter as tk
from tkinter import messagebox

class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = tk.Label(master=self._root, text="Welcome to TaskList!")
        button = tk.Label(master=self._root)

        label.pack()

class List:
    def __init__(self, __name, __status):
        self.__name = __name
        self.__status = __status

    def 

window = tk.Tk()
window.title("Tasklist")

ui = UI(window)
ui.start()

window.mainloop()