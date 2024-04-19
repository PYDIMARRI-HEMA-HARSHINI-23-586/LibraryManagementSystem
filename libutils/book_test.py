# import unittest
from .book import Book, BookDatabase
import pytest


@pytest.fixture
def book_database():
    return BookDatabase()

def test_book_creation():
    book = Book("Title", "Author", "978-0-123456-78-9")
    assert book.title == "Title"
    assert book.author == "Author"
    assert book.isbn == "978-0-123456-78-9"

def test_invalid_isbn():
    with pytest.raises(ValueError):
        Book("Title", "Author", "invalid_isbn")

def test_add_book(book_database):
    book_database.add_book("Test Title", "Test Author", "978-0-123456-78-9")
    assert len(book_database._books) == 1
    assert book_database._books[0].title == "Test Title"
    assert book_database._books[0].author == "Test Author"
    assert book_database._books[0].isbn == "978-0-123456-78-9"

def test_add_book_duplicate_isbn(book_database):
    book_database.add_book("Test Title", "Test Author", "978-0-123456-78-9")
    with pytest.raises(ValueError):
        book_database.add_book("Duplicate Title", "Duplicate Author", "978-0-123456-78-9")

def test_add_book_empty_title(book_database):
    with pytest.raises(ValueError):
        book_database.add_book("", "Test Author", "978-0-123456-78-9")

def test_add_book_empty_author(book_database):
    with pytest.raises(ValueError):
        book_database.add_book("Test Title", "", "978-0-123456-78-9")

def test_add_book_empty_isbn(book_database):
    with pytest.raises(ValueError):
        book_database.add_book("Test Title", "Test Author", "")

# Update the test_list_books test case
def test_list_books(book_database):
    # Add some books to the database
    book_database.add_book("Test Title 1", "Test Author 1", "978-0-123456-78-9")
    book_database.add_book("Test Title 2", "Test Author 2", "978-0-123456-78-0")
    # Update the expected number of books
    assert len(book_database.list_books()) == 2


# Update the test_list_books_with_storage test case
def test_list_books_with_storage(book_database, tmp_path):
    # Add a book to storage
    book_database._storage.save_data([{"title": "Stored Title", "author": "Stored Author", "isbn": "978-0-123456-78-8"}],
                                     str(tmp_path / "test_data.csv"), 
                                     ["title", "author", "isbn"],
                                     "isbn")
    # Update the expected number of books
    assert len(book_database.list_books()) == 1


