from typing import List, Dict

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        """
        Initialize a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self) -> str:
        """
        Return a string representation of the Book object.
        """
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class BookDatabase:
    def __init__(self):
        self._books = []

    def add_book(self, title: str, author: str, isbn: str) -> None:
        """
        Add a book to the database.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        book = Book(title, author, isbn)
        self._books.append(book)

    def list_books(self) -> List[Dict[str, str]]:
        """
        Return details of all books in the database.

        Returns:
            List[Dict[str, str]]: List of dictionaries containing details of all books in the database.
        """
        books_data = []
        for book in self._books:
            books_data.append({
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn
            })
        return books_data

# Global instance of BookDatabase
book_database = BookDatabase()
