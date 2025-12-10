from models import Book, Person
from typing import Dict

class Library:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Library, cls).__new__(cls)
            cls._instance._books = {}
            cls._instance._users = {}
        return cls._instance

    @property
    def books(self) -> Dict[str, Book]:
        return self._books

    @property
    def users(self) -> Dict[str, Person]:
        return self._users

    def add_book(self, book: Book):
        if book.id in self._books:
            raise Exception('Book with this id already exists')
        self._books[book.id] = book

    def add_user(self, user: Person):
        if user.id in self._users:
            raise Exception('User with this id already exists')
        self._users[user.id] = user

    def search(self, strategy, query: str):
        return strategy.search(self, query)

    def lend_book(self, book_id: str, reader_id: str):
        if book_id not in self._books:
            raise Exception('Book not found')
        if reader_id not in self._users:
            raise Exception('Reader not found')
        reader = self._users[reader_id]
        if reader.get_role() != 'Reader':
            raise Exception('Only readers can borrow books')
        book = self._books[book_id]
        reader.borrow(book)
        return True

    def return_book(self, book_id: str, reader_id: str):
        if book_id not in self._books:
            raise Exception('Book not found')
        if reader_id not in self._users:
            raise Exception('Reader not found')
        reader = self._users[reader_id]
        if reader.get_role() != 'Reader':
            raise Exception('Only readers can return books')
        book = self._books[book_id]
        reader.return_book(book)
        return True
