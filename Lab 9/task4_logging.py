import logging
logging.basicConfig(filename="access.log", level=logging.INFO)
print("=== Library Access Panel ===")
username = input("Enter username: ")
role = input("Enter role (Librarian/Reader): ")
if role == "Librarian":
    print("You opened the librarian control panel.")
    logging.info(f"{username} opened librarian panel.")
else:
    print("Access denied. Only Librarian allowed here.")
    logging.warning(f"{username} attempted librarian access without permission.")
