from utils.book import book_database

class BookManagement:
    def add_book(self, title: str, author: str, isbn: str) -> None:
        """
        Add a book to the library.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        book_database.add_book(title, author, isbn)

    def list_books(self) -> None:
        """
        List all books in the library.
        """
        book_database.list_books()
