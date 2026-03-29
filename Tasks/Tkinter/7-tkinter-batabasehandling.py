'''
Database handing, adding, modifying, removing
'''
from tkinter import *
import sqlite3

# First open a new window
root = Tk()
root.title("Database handling")
root.geometry("400x400")
query_label = Label(root)

def query():
    conn = sqlite3.connect("tasklist.db")

    c = conn.cursor()

    c.execute("SELECT task, oid FROM tasks")
    records=c.fetchall()

    print_record = ''

    for record in records:
        print_record += str(record[0]) + " \t " + str(record[1]) + "\n"

    heading_label = Label(root, text="Helvetica", font=("Helvetica", 16))

    heading_label['text'] = "Tasks \t ID"
    heading_label.grid(row=7, column=0, columnspan=2)

    query_label['text'] = print_record
    query_label.grid(row=8, column=0, columnspan=2)

    conn.commit()

    conn.close()

    return None

# Write database new row
def submit():
    conn = sqlite3.connect("tasklist.db")

    c = conn.cursor()

    # Insert into table

    c.execute("INSERT INTO tasks VALUES (:task)",
              {
                  'task' : task.get()
              })
    
    # commit changes
    conn.commit()

    # close connection
    conn.close()

    task.delete(0, END)
    return None

def delete():
    conn = sqlite3.connect("tasklist.db")

    c = conn.cursor()

    c.execute("DELETE FROM tasks WHERE oid=" + delete_box.get())

    delete_box.delete(0, END)
    return None

def edit():
    return None

task_label = Label(root, text="Task")
task_label.grid(row=0, column=0, pady=(10,0))

task = Entry(root, width=30)
task.grid(row=0, column=1, padx=20, pady=(10,0))

submit_bth = Button(root, text="Add new task into database", command=submit)
submit_bth.grid(row=2, column=0, columnspan=2, pady=10, padx=10)

query_bth = Button(root, text="Show tasks", command=query)
query_bth.grid(row=4, column=0, pady=5)

select_label = Label(root, text="Select ID")
select_label.grid(row=4, column=0, pady=5)

delete_box = Entry(root, width=30)
delete_box.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

delete_btn = Button(root, text="Remove task", command=delete)
delete_btn.grid(row=5, column=0, columnspan=2, pady=10, padx=10)

edit_btn = Button(root, text="Edit task", command=edit)
edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10)


root.mainloop()