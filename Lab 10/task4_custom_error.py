class LowPriceError(Exception):
    """Price below 2000 tenge raises this exception."""
    pass

try:
    price = float(input("Enter book price: "))
    if price < 2000:
        raise LowPriceError("Price too low! Book cannot be added.")
    print("Price accepted.")
except ValueError:
    print("Error: Price must be a number.")
except LowPriceError as e:
    print("Custom Exception:", e)
