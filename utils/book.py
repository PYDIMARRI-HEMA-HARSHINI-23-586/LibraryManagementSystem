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

    def list_books(self) -> None:
        """
        Print details of all books in the database.
        """
        for book in self._books:
            print(book)

# Global instance of BookDatabase
book_database = BookDatabase()
