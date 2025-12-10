from abc import ABC, abstractmethod

class Book:
    def __init__(self, book_id: str, title: str, author: str):
        self._id = book_id
        self._title = title
        self._author = author
        self._is_lent = False
        self._borrower_id = None

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def is_lent(self):
        return self._is_lent

    def lend_to(self, borrower_id: str):
        if self._is_lent:
            raise Exception(f"Book '{self._title}' is already lent")
        self._is_lent = True
        self._borrower_id = borrower_id

    def return_from_borrower(self, borrower_id: str):
        if not self._is_lent:
            raise Exception(f"Book '{self._title}' is not lent")
        if self._borrower_id != borrower_id:
            raise Exception("This borrower did not borrow the book")
        self._is_lent = False
        self._borrower_id = None

    def __str__(self):
        status = 'Lent' if self._is_lent else 'Available'
        return f"[{self._id}] '{self._title}' by {self._author} — {status}"


class Person(ABC):
    def __init__(self, person_id: str, name: str):
        self._id = person_id
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_role(self) -> str:
        pass


class Reader(Person):
    def __init__(self, person_id: str, name: str):
        super().__init__(person_id, name)
        self._borrowed_books = []

    def get_role(self) -> str:
        return 'Reader'

    def borrow(self, book: Book):
        book.lend_to(self._id)
        self._borrowed_books.append(book.id)

    def return_book(self, book: Book):
        book.return_from_borrower(self._id)
        self._borrowed_books.remove(book.id)

    def borrowed_books(self):
        return list(self._borrowed_books)


class Staff(Person):
    def __init__(self, person_id: str, name: str):
        super().__init__(person_id, name)

    def get_role(self) -> str:
        return 'Staff'
