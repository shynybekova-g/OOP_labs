import hashlib
def make_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()
original = "book2025"
stored_hash = make_hash(original)
print("Stored password hash:", stored_hash)
print("Check correct password:", make_hash("book2025") == stored_hash)
print("Check wrong password:", make_hash("wrong") == stored_hash)
