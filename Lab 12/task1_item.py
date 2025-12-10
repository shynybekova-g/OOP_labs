from abc import ABC, abstractmethod
class LibraryItem(ABC):
    @abstractmethod
    def title(self):
        pass
    @abstractmethod
    def info(self):
        pass
class Book(LibraryItem):
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self.pages = pages
    def title(self):
        return self.name
    def info(self):
        return f"Кітап: {self.name}, Автор: {self.author}, {self.pages} бет"
class Newspaper(LibraryItem):
    def __init__(self, name, date):
        self.name = name
        self.date = date
    def title(self):
        return self.name
    def info(self):
        return f"Газет: {self.name}, Шыққан күні: {self.date}"
if __name__ == "__main__":
    b = Book("Абай жолы", "М.Әуезов", 450)
    n = Newspaper("Egemen Qazaqstan", "12.02.2024")
    print(b.info())
    print(n.info())
