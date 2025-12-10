from abc import ABC, abstractmethod
class Book(ABC):
    @abstractmethod
    def description(self):
        pass
class Novel(Book):
    def description(self):
        return "Роман: оқырманға қызықты сюжеттік желі ұсынады."
class Textbook(Book):
    def description(self):
        return "Оқу құралы: білім беру мақсатында жазылған."
class Magazine(Book):
    def description(self):
        return "Журнал: жаңалықтар мен мақалалар топтамасы."
books = [Novel(), Textbook(), Magazine()]
for book in books:
    print(book.description())
