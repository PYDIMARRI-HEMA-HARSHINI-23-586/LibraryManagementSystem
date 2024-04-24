"""
Module for checkout functionalities.
"""

from .storage import Storage
from .user import UserDatabase

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
            print(f"\n❌ Error: {e}")
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
        self.users_data =  UserDatabase()
        self._storage = Storage()
        self.books_path = self._storage.books_filepath
        self.users_path = self._storage.users_filepath

    def checkout_book(self) -> None:
        """
        Record a book checkout in the database.

        Args:
            user_id (str): The ID of the user checking out the book.
            isbn (str): The ISBN of the book being checked out.
        """
        try:
            # if not (self._storage.books_exist() and self._storage.users_exist()):
            #     raise ValueError("Database empty. Add books and users.")
            if not (self._storage.books_exist()):
                raise ValueError("No books available in Library, add books.")
            if not (self._storage.users_exist()):
                raise ValueError("No users available in Library, add users.")
        except ValueError as e:
            print(f"\n❌ Error: {e} ❌")
        else:
            user_id, isbn = (input(f"Enter {field}: ") for field in ["user ID", "ISBN"])
            
            try:
                if not user_id.strip():
                    raise ValueError("User ID cannot be empty")
                if not isbn.strip():
                    raise ValueError("ISBN cannot be empty")
            except ValueError as e:
                print(f"\n❌ Error: {e} ❌")
            else:
                checkout = Checkout(user_id, isbn)
                self._checkouts.append(checkout)
            existing_books = self._storage.load_data(self.books_path)
            existing_isbns = [book["isbn"] for book in existing_books]
            
            existing_users = self._storage.load_data(self.users_path)
            existing_ids = [user["UserID"] for user in existing_users]
            existing_userIDs = [user["UserID"] for user in existing_users]
            try:
                book_index = existing_isbns.index(isbn)
                if existing_books[book_index]['AvailableInLibrary'] != 'No':
                    existing_books[book_index]['AvailableInLibrary'] = 'No'
                else:
                    raise ValueError("This Book already checkedout.")
                self._storage.save_data(data = existing_books, filepath = self.books_path,fieldnames=None, unique_key = None, mode = 'w')
                
                for id in existing_userIDs:
                    if int(id) == int(user_id):
                        check_id = id
                        break
                
                user_index = existing_ids.index(check_id)
                inhad_val = existing_users[user_index]['BookInHand']
                
        
                if not inhad_val:
                    existing_users[user_index]['BookInHand'] = isbn
                elif isbn in inhad_val:
                    raise ValueError(f"{existing_users[user_index]['Name']}'s userID: {id} , already has same book.")                    
                else:
                    existing_users[user_index]['BookInHand'] = f"{inhad_val}, f{isbn}"
                
                check_save_data = self._storage.save_data(data = existing_users, filepath = self.users_path,fieldnames=None, unique_key = None, mode = 'w')
                if check_save_data:
                    print("Book checked out ✅.")
                
            except ValueError as e:
                if "is not in list" in str(e).strip():
                    print(f"\n❌ Error: Enter valid userID or ISBN ❌")
                else:
                    print(f"\n❌ Error: {e} ❌")
                # print(f"isbn {isbn} not found in the library database.")
        
        
        

    def get_checkouts(self) -> list:
        """
        Retrieve all book checkouts from the database.

        Returns:
            list: List of Checkout objects representing book checkouts.
        """
        return self._checkouts

# Global instance of CheckoutDatabase
checkout_database = CheckoutDatabase()
