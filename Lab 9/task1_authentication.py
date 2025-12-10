import hashlib
users = {
    "librarian": {
        "password": hashlib.sha256("library123".encode()).hexdigest(),
        "role": "Librarian"
    },
    "reader": {
        "password": hashlib.sha256("book2025".encode()).hexdigest(),
        "role": "Reader"
    }
}
print("=== Library Login System ===")
username = input("Username: ")
password = input("Password: ")
hashed_password = hashlib.sha256(password.encode()).hexdigest()
if username in users and users[username]["password"] == hashed_password:
    print("Login successful.")
    print("Your role:", users[username]["role"])
else:
    print("Login failed. Incorrect username or password.")
