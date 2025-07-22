import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', 'admin123')")

user_input = input("Enter username: ")
pass_input = input("Enter password: ")

query = f"SELECT * FROM users WHERE username='{user_input}' AND password='{pass_input}'"
cursor.execute(query)
result = cursor.fetchone()

if result:
    print("Logged in!")
else:
    print("Login failed.")
