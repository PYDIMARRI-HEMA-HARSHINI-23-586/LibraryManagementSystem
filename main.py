"""
Date: 18 April 2024
Author: Pavan Kumar
Project: library management system
"""
from book_management import BookManagement
from user_management import UserManagement
from checkout_management import CheckoutManagement
from libutils.storage import Storage

class LibraryManagementSystem:
    def __init__(self):
        """
        Initializes the Library Management System.

        Attributes:
            book_manager (BookManagement): Manages books in the library.
            user_manager (UserManagement): Manages users in the library.
            checkout_manager (CheckoutManagement): Manages the checkout process.
            storage (Storage): Handles data storage.
        """
        self.book_manager = BookManagement()
        self.user_manager = UserManagement()
        self.checkout_manager = CheckoutManagement()
        self.storage = Storage()

    def display_main_menu(self) -> str:
        """
        Display the main menu options and get the user's choice.

        Returns:
            str: The user's choice.
        """
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. List Books")
        print("3. Add User")
        print("4. List Users")
        print("5. Checkout Book")
        print("6. Exit")
        return input("Enter choice: ")

    def add_book(self, title: str, author: str, isbn: str) -> None:
        """
        Adds a book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.book_manager.add_book(title, author, isbn)

    def list_books(self) -> None:
        """Lists all the books in the library."""
        books = self.book_manager.list_books()
        if books:
            for index, book in enumerate(books, start=1):
                print(f"Book {index}:\nTitle: {book['title']}\nAuthor: {book['author']}\nISBN: {book['isbn']}\nAvailableInLibrary: {book['AvailableInLibrary']}\n-------------------------")
        else:
            print("No Books in the library, Please add books.")

    def add_user(self, name: str, user_id: str) -> None:
        """
        Adds a user to the library.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        self.user_manager.add_user(name, user_id)
        

    def list_users(self) -> None:
        """Lists all the users registered in the library."""
        users = self.user_manager.list_users()
        if users:
            for index, user_info in enumerate(users, start=1):
                all_books = ", ".join(user_info['BookInHand']) if user_info['BookInHand'] else "Nothing"
                print(f"UserID {user_info['UserID']}:\nName: {user_info['Name']}\nBooksInHand: {all_books}\n-------------------------")
        else:
            print("No Users in the library, Please add users.")

    def checkout_book(self, user_id: str, isbn: str) -> None:
        """
        Handles the checkout process for a book.

        Args:
            user_id (str): The ID of the user.
            isbn (str): The ISBN of the book to be checked out.
        """
        self.checkout_manager.checkout_book(user_id, isbn)
        print("Book checked out.")

    def run(self) -> None:
        """Main function to run the library management system."""
        while True:
            choice = self.display_main_menu()
            if choice == '1':
                self.add_book(*(input(f"Enter {field}: ") for field in ["title", "author", "isbn"]))
            elif choice == '2':
                print("\n-------------------------\nList of books in Library:\n-------------------------")
                self.list_books()
            elif choice == '3':
                self.add_user(*(input(f"Enter {field}: ") for field in ["name", "user ID"]))
            elif choice == '4':
                print("\n-------------------------\nList of users registered in Library:\n-------------------------")
                self.list_users()
            elif choice == '5':
                self.checkout_book(*(input(f"Enter {field}: ") for field in ["user ID", "ISBN"]))
            elif choice == '6':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
        lib_data, users_data = self.book_manager.list_books(), self.user_manager.list_users()
        self.storage.save_system_state(books=lib_data, users=users_data)

if __name__ == "__main__":
    LibraryManagementSystem().run()
