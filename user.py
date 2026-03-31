class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def display_user(self):
        print(f"User ID: {self.user_id}, Name: {self.name}")

    def borrow_book(self, book):
        if book.available:
            book.update_status(False)
            print("Book borrowed successfully!")
        else:
            print("Book not available!")

    def return_book(self, book):
        book.update_status(True)
        print("Book returned successfully!")

    def to_file_format(self):
        return f"{self.user_id},{self.name}\n"