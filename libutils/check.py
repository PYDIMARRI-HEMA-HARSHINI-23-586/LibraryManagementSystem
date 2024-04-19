"""
Module for checkout functionalities.
"""

from .storage import Storage

class Checkout:
    """
    Represents a book checkout.
    """
    
    def __init__(self, user_id: str, isbn: str):
        """
        Initialize a Checkout object.

        Args:
            user_id (str): The ID of the user.
            isbn (str): The ISBN of the book being checked out.
        """
        try:
            if not user_id.strip() and not isbn.strip():
                raise ValueError("User ID and ISBN cannot be empty")
            if not user_id.strip():
                raise ValueError("User ID cannot be empty")
            if not isbn.strip():
                raise ValueError("ISBN cannot be empty")
        except ValueError as e:
            print(f"Error: {e}")
            self.user_id = None
            self.isbn = None
        else:
            self.user_id = user_id
            self.isbn = isbn

class CheckoutDatabase:
    """
    Database for managing book checkouts.
    """
    
    def __init__(self):
        self._checkouts = []
        self._storage = Storage()
        self.books_path = self._storage.books_filepath
        self.users_path = self._storage.users_filepath

    def checkout_book(self, user_id: str, isbn: str) -> None:
        """
        Record a book checkout in the database.

        Args:
            user_id (str): The ID of the user checking out the book.
            isbn (str): The ISBN of the book being checked out.
        """
        try:
            if not user_id.strip():
                raise ValueError("User ID cannot be empty")
            if not isbn.strip():
                raise ValueError("ISBN cannot be empty")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            checkout = Checkout(user_id, isbn)
            self._checkouts.append(checkout)
        existing_books = self._storage.load_data(self.books_path)
        existing_isbns = [book["isbn"] for book in existing_books]
        
        existing_users = self._storage.load_data(self.users_path)
        existing_ids = [user["UserID"] for user in existing_users]
        try:
            book_index = existing_isbns.index(isbn)
            existing_books[book_index]['AvailableInLibrary'] = 'No'
            self._storage.save_data(data = existing_books, filepath = self.books_path,fieldnames=None, unique_key = None, mode = 'w')
            
            
            user_index = existing_ids.index(isbn)
            inhad_val = existing_users[user_index]['BookInHand']
    
            if not inhad_val:
                existing_users[user_index]['BookInHand'] = isbn
            else:
                existing_users[user_index]['BookInHand'] = f"{inhad_val}, f{isbn}"
            
            self._storage.save_data(data = existing_users, filepath = self.users_path,fieldnames=None, unique_key = None, mode = 'w')
            
        except ValueError as e:
            print(f"\nError: {e}")
            print(f"isbn {isbn} not found in the library database.")
        
        
        

    def get_checkouts(self) -> list:
        """
        Retrieve all book checkouts from the database.

        Returns:
            list: List of Checkout objects representing book checkouts.
        """
        return self._checkouts

# Global instance of CheckoutDatabase
checkout_database = CheckoutDatabase()
