import sqlite3
conn = sqlite3.connect("library_users.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
conn.commit()
cur.execute("SELECT * FROM users WHERE username='librarian'")
if cur.fetchone() is None:
    cur.execute("INSERT INTO users VALUES (?, ?)", ("librarian", "library123"))
    cur.execute("INSERT INTO users VALUES (?, ?)", ("reader", "book2025"))
    conn.commit()
    print("Database created with sample accounts.")
print("=== Library Login (Safe SQL) ===")
u = input("Username: ")
p = input("Password: ")
cur.execute("SELECT * FROM users WHERE username=? AND password=?", (u, p))
result = cur.fetchone()
if result:
    print("Access granted.")
else:
    print("Access denied.")
conn.close()
