"""Module for managing books in the library."""

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
        try:
            if not title.strip() and not author.strip() and not isbn.strip():
                raise ValueError("Book information is incomplete")
            if not title.strip():
                raise ValueError("Title cannot be empty")
            if not author.strip():
                raise ValueError("Author cannot be empty")
            if not isbn.strip():
                raise ValueError("ISBN cannot be empty")
        except ValueError as e:
            print(f"Error: {e}")
            self.title = None
            self.author = None
            self.isbn = None
        else:
            self.title = title
            self.author = author
            self.isbn = isbn
            self.AvailableInLibrary = "Yes"

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
        try:
            if isbn in [book.isbn for book in self._books]:
                raise ValueError("Book with the same ISBN already exists.")
            if not title:
                raise ValueError("Title cannot be empty")
            if not author:
                raise ValueError("Author cannot be empty")
            if not isbn:
                raise ValueError("ISBN cannot be empty")
        except ValueError as e:
            print(f"\nError: {e}")
        else:
            book = Book(title, author, isbn)
            self._books.append(book)
            print("\nBook added.")
    
    def list_books(self) -> List[Dict[str, str]]:
        """
        Return details of all books in the database.

        Returns:
            List[Dict[str, str]]: List of dictionaries containing details of all books in the database.
        """
        books_data = []
        if self._books:
            for book in self._books:
                books_data.append({
                    "title": book.title,
                    "author": book.author,
                    "isbn": book.isbn,
                    "AvailableInLibrary":book.AvailableInLibrary
                })
        if self._storage.books_exist():
            books_path = self._storage.books_filepath
            loaded_books_data = self._storage.load_data(books_path)
            if loaded_books_data:
                books_data.extend(loaded_books_data)
        return books_data
            
# Global instance of BookDatabase
book_database = BookDatabase()
