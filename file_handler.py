from book import Book

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def save_books(self, books):
        with open(self.filename, 'w') as file:
            for book in books:
                file.write(book.to_file_format())

    def load_books(self):
        books = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    books.append(Book.from_file_format(line))
        except FileNotFoundError:
            print("File not found, starting fresh.")
        return books