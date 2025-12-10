from abc import ABC, abstractmethod

class SearchStrategy(ABC):
    @abstractmethod
    def search(self, library, query: str):
        pass

class SearchByTitle(SearchStrategy):
    def search(self, library, query: str):
        q = query.strip().lower()
        return [b for b in library.books.values() if q in b.title.lower()]

class SearchByAuthor(SearchStrategy):
    def search(self, library, query: str):
        q = query.strip().lower()
        return [b for b in library.books.values() if q in b.author.lower()]
