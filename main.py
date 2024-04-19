"""
Date: 18 April 2024
Author: Pavan Kumar
Project: library management system
"""
from book_management import BookManagement
from user_management import UserManager
from checkout_management import CheckoutManagement  
from utils.storage import Storage

class LibraryManagementSystem:
    def __init__(self):
        self.book_manager = BookManagement()
        self.user_manager = UserManager()
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
        print("4. User database")
        print("5. Checkout Book")
        print("6. Exit")
        return input("Enter choice: ")

    def run(self) -> None:
        """
        Main function to run the library management system.
        """
        while True:
            choice = self.display_main_menu()
            if choice == '1':
                self.book_manager.add_book(*(input(f"Enter {field}: ") for field in ["title", "author", "isbn"]))
            elif choice == '2':
                print("\n-------------------------\nList of books in Library:\n-------------------------")
                if self.book_manager.list_books():
                    for index, book in enumerate(self.book_manager.list_books(), start=1):
                        print(f"Book {index}:\nTitle: {book['title']}\nAuthor: {book['author']}\nISBN: {book['isbn']}\nAvailableInLibrary: {book['AvailableInLibrary']}\n-------------------------")
                else:
                    print("No Books in the library, Please add books.")
            elif choice == '3':
                self.user_manager.add_user(*(input(f"Enter {field}: ") for field in ["name", "user ID"]))
                print("User added.")
            elif choice == '4':
                print("\n-------------------------\nList of users registerd in Library:\n-------------------------")
                if self.user_manager.list_users():
                    for index, user_info in enumerate(self.user_manager.list_users(), start=1):
                        print(f"UserID {user_info['UserID']}:\nName: {user_info['Name']}\nBooksInHand: {user_info['BooksInHand']}\nTimestamp: {user_info['Timestamp']}\n-------------------------")
                else:
                    print("No Books in the library, Please add books.")
                print("User added.")
            elif choice == '5':
                self.checkout_manager.checkout_book(*(input(f"Enter {field}: ") for field in ["user ID", "ISBN"]))
                print("Book checked out.")
            elif choice == '6':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
        lib_data, users_data = self.book_manager.list_books(), self.user_manager.list_users()
        self.storage.save_system_state(books=lib_data, users=users_data)

if __name__ == "__main__":
    LibraryManagementSystem().run()
