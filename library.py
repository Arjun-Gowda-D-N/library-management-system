from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    # Add book
    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    # View books
    def view_books(self):
        if not self.books:
            print("No books available.")
        for book in self.books:
            book.display_book()

    # Add user
    def add_user(self, user):
        self.users.append(user)
        print("User added successfully!")

    # Issue book
    def issue_book(self, book_id, user_id):
        try:
            book = next(b for b in self.books if b.book_id == book_id)
            user = next(u for u in self.users if u.user_id == user_id)

            if book.available:
                user.borrow_book(book)
            else:
                print("Book is already issued!")

        except StopIteration:
            print("Book or User not found!")

    # Return book
    def return_book(self, book_id):
        try:
            book = next(b for b in self.books if b.book_id == book_id)
            if not book.available:
                book.update_status(True)
                print("Book returned successfully!")
            else:
                print("Book was not issued!")

        except StopIteration:
            print("Book not found!")