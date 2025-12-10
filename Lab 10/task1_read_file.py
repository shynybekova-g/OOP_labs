try:
    with open(r"C:\Users\Student\Documents\Lab_10_File_Handling\books.txt", "r", encoding="utf-8") as file:
        prices = []
        for line in file:
            title, price = line.strip().split(", ")
            price_float = float(price)
            prices.append(price_float)
            print(f"{title} - {price_float} tenge")
        average_price = sum(prices) / len(prices)
        print(f"Average price: {average_price:.2f} tenge")
except FileNotFoundError:
    print("Error: file 'books.txt' not found.")
except Exception as e:
    print("Other error:", e)
