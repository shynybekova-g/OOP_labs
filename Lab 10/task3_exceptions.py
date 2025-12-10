try:
    with open(r"C:\Users\Student\Documents\Lab_10_File_Handling\books.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
        print("File found. Reading successful.")
except FileNotFoundError:
    print("Error: file not found.")
except Exception as e:
    print("Other error:", e)
else:
    print("File read completed successfully.")
finally:
    print("Program finished.")
