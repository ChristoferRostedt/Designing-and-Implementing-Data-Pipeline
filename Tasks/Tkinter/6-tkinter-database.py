'''
Create new new database and database tables
'''

from tkinter import *
import sqlite3

root = Tk()
root.title("Database")
root.geometry("400x400")

# Create database named tasklist
conn = sqlite3.connect("tasklist.db")

c = conn.cursor()

# Remove database table named task if it already exist
c.execute("DROP TABLE IF EXISTS tasks")

# Create table
sql = ''' CREATE TABLE tasks (
    task VARCHAR (255)
)'''

c.execute(sql)

# Commit changes
conn.commit()

# Close database connection
conn.close()

root.mainloop()