"""Module for managing books in the library."""

from libutils.book import book_database

class BookManagement:
    """
    Class for managing books in the library.
    """
    
    def add_book(self, title: str, author: str, isbn: str) -> None:
        """
        Add a book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        book_database.add_book(title, author, isbn)

    def list_books(self) -> list:
        """
        List all books in the library.

        Returns:
            list: A list of dictionaries containing book information.
        """
        return book_database.list_books()
