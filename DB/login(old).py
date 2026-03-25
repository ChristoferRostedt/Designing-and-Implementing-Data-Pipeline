import sqlite3
conn = sqlite3.connect("school copy.db")
cursor = conn.cursor()

def showMenu() -> None:
    print("1 - Register")
    print("2 - Login")
    print("0 - Exit")

def get_student_credits(student_id) -> None:
    return None

def create_table():
    query = "DROP TABLE IF EXISTS login"
    cursor.execute(query)
    conn.commit()
    
    query = "CREATE TABLE login(Username VARCHAR UNIQUE, Password VARCHAR)"
    cursor.execute(query)
    conn.commit()

def enter(username, password):
    query = "INSERT INTO login (Username, Password) VALUES (?, ?)"
    cursor.execute(query, (username, password))
    conn.commit()

def check(username, password):
    query = 'SELECT * FROM login WHERE Username = ? AND Password = ?'
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.commit()
    print('[DEBUG][check] result:', result)
    return result

def loginlol():

    username = input("Username: ")
    password = input("Password: ")
    if check(username, password):
        print("Username correct!")
        print("Password correct!")
        print("Logging in...")
    else:
        print("Something wrong")

# --- main ---
def main() -> None:
    print("Program starting.")
    while True:
        showMenu()
        choice = input("Insert option: ")
        try:
            choice = int(choice)
        except ValueError:
            print("Value must be an integer.")

        if(choice == 1):
            create_table()
            Username = input("Create username: ")
            Password = input("Create password: ")
            enter(Username, Password)
            #check(Username, Password)
            print()

        elif(choice == 2):
            loginlol()
            cursor.close()
            conn.close()
            print()

        elif(choice == 0):
            print("Exiting...\n")
            break
        else:
            print("Unknown option. Try again!\n")
    
    print("Program ending.")

if __name__ == "__main__":
    main()