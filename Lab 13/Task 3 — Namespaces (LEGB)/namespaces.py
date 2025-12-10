x = "Global"
def outer():
    x = "Enclosing"
    def inner():
        x = "Local"
        print("Local:", x)
    inner()
    print("Enclosing:", x)
outer()
print("Global:", x)
