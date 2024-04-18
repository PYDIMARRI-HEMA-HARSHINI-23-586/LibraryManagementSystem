"""
Date: 18 April 2024
Author: Pavan Kumar
Project: Student library management system
"""
from book_management import BookManagement  # Importing BookManagement class
from user_management import UserManager
from checkout_management import CheckoutManagement

class LibraryManagementSystem:
    def __init__(self):
        self.book_manager = BookManagement()  # Creating an instance of BookManagement
        self.user_manager = UserManager()
        self.checkout_manager = CheckoutManagement()

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
        print("4. Checkout Book")
        print("5. Exit")
        choice = input("Enter choice: ")
        return choice

    def run(self) -> None:
        """
        Main function to run the library management system.
        """
        while True:
            choice = self.display_main_menu()
            if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                self.book_manager.add_book(title, author, isbn)  # Using BookManagement to add a book
                print("Book added.")
            elif choice == '2':
                self.book_manager.list_books()  # Using BookManagement to list books
            elif choice == '3':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                self.user_manager.add_user(name, user_id)
                print("User added.")
            elif choice == '4':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                self.checkout_manager.checkout_book(user_id, isbn)
                print("Book checked out.")
            elif choice == '5':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")


if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    library_system.run()
