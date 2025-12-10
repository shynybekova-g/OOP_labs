from models import Book
from library import Library
from user_factory import UserFactory
from search import SearchByTitle, SearchByAuthor

def demo():
    lib = Library()

    # Add books
    lib.add_book(Book('B1', 'The Great Gatsby', 'F. Scott Fitzgerald'))
    lib.add_book(Book('B2', 'A Tale of Two Cities', 'Charles Dickens'))
    lib.add_book(Book('B3', 'Great Expectations', 'Charles Dickens'))

    # Add users
    alice = UserFactory.create_user('reader', 'U1', 'Alice')
    bob = UserFactory.create_user('reader', 'U2', 'Bob')
    staff = UserFactory.create_user('staff', 'S1', 'Librarian')

    lib.add_user(alice)
    lib.add_user(bob)
    lib.add_user(staff)

    # Search by title
    print('\nSearch by title "great":')
    results = lib.search(SearchByTitle(), 'great')
    for b in results:
        print('  ', b)

    # Search by author
    print('\nSearch by author "Charles Dickens":')
    results = lib.search(SearchByAuthor(), 'Charles Dickens')
    for b in results:
        print('  ', b)

    # Lend a book
    print('\nLending book B1 to Alice (U1)')
    lib.lend_book('B1', 'U1')
    print('  Book B1 status:', lib.books['B1'])

    # Try lending same book again (should raise Exception)
    try:
        print('\nAttempting to lend B1 to Bob (U2)')
        lib.lend_book('B1', 'U2')
    except Exception as e:
        print('  Expected error:', e)

    # Return the book
    print('\nAlice returns B1')
    lib.return_book('B1', 'U1')
    print('  Book B1 status:', lib.books['B1'])

if __name__ == '__main__':
    demo()
