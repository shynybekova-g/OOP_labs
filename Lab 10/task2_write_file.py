file_path = r"C:\Users\Student\Documents\Lab_10_File_Handling\books.txt"

title = input("Enter book title: ")
price = input("Enter book price: ")

if not price.isdigit():
    print("Error: Price must be a number.")
else:
    try:
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"\n{title}, {price}")
        print("Record added successfully!")

        with open(file_path, "r", encoding="utf-8") as file:
            print("\nUpdated book list:")
            for line in file:
                print(line.strip())

    except Exception as e:
        print("Error occurred:", e)
