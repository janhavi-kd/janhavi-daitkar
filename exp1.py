class Book:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False

class Patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []

class Library:
    def __init__(self):
        self.books = {}
        self.patrons = {}

    def add_book(self, isbn, title, author):
        self.books[isbn] = Book(isbn, title, author)

    def register_patron(self, patron_id, name):
        self.patrons[patron_id] = Patron(patron_id, name)

    def borrow_book(self, patron_id, isbn):
        patron = self.patrons[patron_id]
        book = self.books[isbn]
        
        if not book.is_borrowed:
            book.is_borrowed = True
            patron.borrowed_books.append(book)
            print(f"{patron.name} borrowed {book.title}")
        else:
            print(f"{book.title} is already out")

    def return_book(self, patron_id, isbn):
        patron = self.patrons[patron_id]
        book = self.books[isbn]
        
        book.is_borrowed = False
        patron.borrowed_books.remove(book)
        print(f"{patron.name} returned {book.title}")

# --- Execution ---
library = Library()

library.add_book("101", "joker", "witch")
library.register_patron("P1", "shree")
library.borrow_book("P1", "101")
library.return_book("P1", "101")