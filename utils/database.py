import sqlite3
from datetime import date


def create_db():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS passwords(password text primary key, data text)")

    connection.commit()
    connection.close()


def get_db():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM passwords")
    collection = [{'password': row[0], 'date': row[1]} for row in cursor.fetchall()]

    connection.close()

    return collection

def show_all():
    collection = get_db()
    if collection == []:
        print("Your collection is empty")
    else:
        for password in collection:
            print(f"""Password - {password['password']}
Date - {password['date']}
""")


def show_last():
    collection = get_db()
    if collection == []:
        print("Your collection is empty")
    else:
            print(f"""Password - {collection[-1]['password']}
Date - {collection[-1]['date']}""")

def add_password(password):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO passwords VALUES(?,?)", (password, date.today()))

    connection.commit()
    connection.close()

def delete_password():
    password = input("Input the password to delete or input 'ALL' to delete all passwords: ")
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    if password == 'ALL':
        cursor.execute('DELETE FROM passwords')
    else:
        cursor.execute("DELETE FROM passwords WHERE password = ?", (password,))

    connection.commit()
    connection.close()




