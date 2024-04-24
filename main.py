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
        print(f"\n-------------------------------\n🏛️ Library Management System 🏛️\n-------------------------------")
        print("1. 🆕 Add Book")
        print("2. 📚 List Books")
        print("3. 🆕 Add User")
        print("4. 📜 List Users")
        print("5. ✅ Checkout Book")
        print("6. ⛔ Exit")
        return input("Enter choice: ")

    def add_book(self, title: str, author: str, isbn: str) -> None:
            """
            Adds a book to the library.

            Args:
                title (str): The title of the book.
                author (str): The author of the book.
                isbn (str): The ISBN of the book.
            """
            try:
                self.book_manager.add_book(title, author, isbn)
            except ValueError as e:
                if str(e).strip() == "Invalid ISBN":
                    print(f"\n❌ Error: {e} ❌")
                    print("Valid ISBN example: 978-0-123456-78-9")
                elif str(e).strip() == "Book with the same ISBN already exists.":
                    print(f"\n❌ Error: {e} ❌")
                    print(self.list_books())
                else:
                    print(f"\n❌ Error: {e} ❌")

    def checkout_book(self) -> None:
        """
        Handles the checkout process for a book.

        Args:
            user_id (str): The ID of the user.
            isbn (str): The ISBN of the book to be checked out.
        """
        try:
            self.checkout_manager.checkout_book()
        except ValueError as e:
            print(f"\n❌ Error: {e} ❌")

    def list_books(self) -> None:
        """Lists all the books in the library."""
        books = self.book_manager.list_books()
        if books:
            print("\n-------------------------\nList of books in Library:\n-------------------------")
            for index, book in enumerate(books, start=1):
                print(f"Book {index}:\nTitle: {book['title']}\nAuthor: {book['author']}\nISBN: {book['isbn']}\nAvailableInLibrary: {book['AvailableInLibrary']}\n-------------------------")
        else:
            print("\n------------------------------------------------\n⚠️ No Books in the library, Please add books ⚠️\n------------------------------------------------")

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
            self.user_manager.print_users_database(users)
        else:
            print("\n------------------------------------------------\n⚠️ No Users in the library, Please add users ⚠️\n------------------------------------------------")


    def run(self) -> None:
        """Main function to run the library management system."""
        while True:
            choice = self.display_main_menu()
            if choice == '1':
                self.add_book(*(input(f"Enter {field}: ") for field in ["title", "author", "isbn"]))
            elif choice == '2':
                self.list_books()
            elif choice == '3':
                self.add_user(*(input(f"Enter {field}: ") for field in ["name", "user ID"]))
            elif choice == '4':
                self.list_users()
            elif choice == '5':
                self.checkout_book()
            elif choice == '6':
                print("\n-------------------------\n🚧 Application Closed 🚧\n-------------------------")
                break
            else:
                print("\n--------------------------------------\n⚠️ Invalid choice, please try again ⚠️\n--------------------------------------")
        lib_data, users_data = self.book_manager.list_books(), self.user_manager.list_users()
        self.storage.save_system_state(books=lib_data, users=users_data)

if __name__ == "__main__":
    LibraryManagementSystem().run()
