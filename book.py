class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def display_book(self):
        print(f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Available: {self.available}")

    def update_status(self, status):
        self.available = status

    def to_file_format(self):
        return f"{self.book_id},{self.title},{self.author},{self.available}\n"

    @staticmethod
    def from_file_format(data):
        book_id, title, author, available = data.strip().split(',')
        return Book(book_id, title, author, available == 'True')