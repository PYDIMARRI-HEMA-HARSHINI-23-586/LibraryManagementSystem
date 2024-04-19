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
                self.book_manager.add_book(title, author, isbn)
                
            elif choice == '2':
                print("-------------------------")
                print("List of books in Library:")
                print("-------------------------")
                books_data = self.book_manager.list_books()
                for index, book in enumerate(books_data, start=1):
                    print(f"Book {index}:")
                    print(f"Title: {book['title']}")
                    print(f"Author: {book['author']}")
                    print(f"ISBN: {book['isbn']}")
                    print("-------------------------")
            elif choice == '3':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                self.user_manager.add_user(name, user_id)
                print("User added.")
            elif choice == '4':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                self.checkout_manager.checkout_book(user_id, isbn)  # Using CheckoutManagement to checkout a book
                print("Book checked out.")
            elif choice == '5':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")
        lib_data, users_data = self.book_manager.list_books(), self.user_manager.list_users()
        return lib_data, users_data


if __name__ == "__main__":
    library_system = LibraryManagementSystem()
    lib_data, users_data = library_system.run()
    
    # Create an instance of the Storage class
    storage = Storage()
    # Call the save_system_state method on the storage instance
    storage.save_system_state(books=lib_data, users=users_data)

