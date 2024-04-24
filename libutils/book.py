"""Module for managing books in the library."""
import re
from typing import List, Dict
from .storage import Storage

class Book:
    """Class representing a book in the library."""

    def __init__(self, title: str, author: str, isbn: str):
        """
        Initialize a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.title = None
        self.author = None
        self.isbn = None
        self.AvailableInLibrary = "Yes"
        
        self.validate_and_set_book_info(title, author, isbn)

    def validate_and_set_book_info(self, title: str, author: str, isbn: str):
        """
        Validate the input information and set book attributes if valid.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        if not title.strip() or not author.strip() or not isbn.strip():
            raise ValueError("Book information is incomplete")
        if not isinstance(title, str) or not isinstance(author, str) or not isinstance(isbn, str):
            raise TypeError("Title, author, and ISBN must be strings")
        if not self.validate_isbn(isbn):
            raise ValueError("Invalid ISBN")

        self.title = title
        self.author = author
        self.isbn = isbn

    def validate_isbn(self, isbn: str) -> bool:
        """
        Validate the ISBN using a regular expression.

        Args:
            isbn (str): The ISBN to validate.

        Returns:
            bool: True if the ISBN is valid, False otherwise.
        """
        isbn_pattern = r"^(978|979)-\d{1,5}-\d{1,7}-\d{1,7}-\d$"
        return bool(re.match(isbn_pattern, isbn))

    def __str__(self) -> str:
        """
        Return a string representation of the Book object.
        """
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class BookDatabase:
    """Class representing a database of books."""

    def __init__(self):
        """Initialize the BookDatabase."""
        self._books = []
        self._storage = Storage()

    def add_book(self, title: str, author: str, isbn: str) -> None:
        """
        Add a book to the database.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        if isbn in [book.isbn for book in self._books]:
            raise ValueError("Book with the same ISBN already exists.")
        if isbn in [entry['isbn'] for entry in self.list_books()]:
            raise ValueError("Book with the same ISBN already exists.")
        if not title:
            raise ValueError("Title cannot be empty")
        if not author:
            raise ValueError("Author cannot be empty")
        if not isbn:
            raise ValueError("ISBN cannot be empty")
            
        book = Book(title, author, isbn)
        self._books.append(book)
        print("\nBook added successfully ✅.")

    def list_books(self) -> List[Dict[str, str]]:
        """
        Return details of all books in the database.

        Returns:
            List[Dict[str, str]]: List of dictionaries containing details of all books in the database.
        """
        books_data = []
                
        if self._books:
            # Append books from the database
            for book in self._books:
                books_data.append({
                    "title": book.title,
                    "author": book.author,
                    "isbn": book.isbn,
                    "AvailableInLibrary": book.AvailableInLibrary
                })
        
        # Append loaded books from storage
        if self._storage.books_exist():
            books_path = self._storage.books_filepath
            loaded_books_data = self._storage.load_data(books_path)
            if loaded_books_data:
                for loaded_book in loaded_books_data:
                    # Ensure that the loaded book contains necessary fields
                    if all(field in loaded_book for field in ["title", "author", "isbn"]):
                        books_data.append({
                            "title": loaded_book["title"],
                            "author": loaded_book["author"],
                            "isbn": loaded_book["isbn"],
                            "AvailableInLibrary": loaded_book.get("AvailableInLibrary", "Unknown")
                        })
        
        return books_data
            
# Global instance of BookDatabase
book_database = BookDatabase()
