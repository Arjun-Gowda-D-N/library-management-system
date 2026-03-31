from library import Library
from book import Book
from user import User
from file_handler import FileHandler

def main():
    library = Library()
    file_handler = FileHandler("books.txt")

    # Load existing books
    library.books = file_handler.load_books()

    while True:
        print("\n===== Library Menu =====")
        print("       1. Add Book")
        print("       2. View Books")
        print("       3. Add User")
        print("       4. Issue Book")
        print("       5. Return Book")
        print("       6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Title: ")
            author = input("Enter Author: ")
            book = Book(book_id, title, author)
            library.add_book(book)

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            user_id = input("Enter User ID: ")
            name = input("Enter Name: ")
            user = User(user_id, name)
            library.add_user(user)

        elif choice == '4':
            book_id = input("Enter Book ID: ")
            user_id = input("Enter User ID: ")
            library.issue_book(book_id, user_id)

        elif choice == '5':
            book_id = input("Enter Book ID: ")
            library.return_book(book_id)

        elif choice == '6':
            file_handler.save_books(library.books)
            print("Data saved. Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()