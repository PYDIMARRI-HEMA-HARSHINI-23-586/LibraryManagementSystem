import unittest
import os
from utils.book import Book, BookDatabase
from utils.user import User, UserDatabase
from utils.storage import Storage


class TestBook(unittest.TestCase):
    def test_book_initialization(self):
        # Test initialization with valid arguments
        book = Book("Title", "Author", "ISBN")
        self.assertEqual(book.title, "Title")
        self.assertEqual(book.author, "Author")
        self.assertEqual(book.isbn, "ISBN")

        # Test initialization with empty title
        with self.assertRaises(ValueError):
            Book("", "Author", "ISBN")

        # Test initialization with empty author
        with self.assertRaises(ValueError):
            Book("Title", "", "ISBN")

        # Test initialization with empty ISBN
        with self.assertRaises(ValueError):
            Book("Title", "Author", "")

        # Test initialization with all arguments empty
        with self.assertRaises(ValueError):
            Book("", "", "")

    # Add more test cases as needed for edge cases and additional functionalities

class TestBookDatabase(unittest.TestCase):
    def setUp(self):
        # Initialize a BookDatabase instance for each test case
        self.book_database = BookDatabase()

    def test_add_book(self):
        # Test adding a new book
        self.book_database.add_book("Title", "Author", "ISBN")
        self.assertEqual(len(self.book_database._books), 1)

        # Test adding a book with the same ISBN
        with self.assertRaises(ValueError):
            self.book_database.add_book("Title2", "Author2", "ISBN")

        # Test adding a book with empty title
        with self.assertRaises(ValueError):
            self.book_database.add_book("", "Author", "ISBN")

        # Test adding a book with empty author
        with self.assertRaises(ValueError):
            self.book_database.add_book("Title", "", "ISBN")

        # Test adding a book with empty ISBN
        with self.assertRaises(ValueError):
            self.book_database.add_book("Title", "Author", "")

    # Add more test cases as needed for other functionalities

class TestUser(unittest.TestCase):
    def test_user_initialization(self):
        # Test initialization with valid arguments
        user = User("John Doe", "123")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.user_id, "123")

        # Test initialization with empty name
        with self.assertRaises(ValueError):
            User("", "123")

        # Test initialization with empty user ID
        with self.assertRaises(ValueError):
            User("John Doe", "")

        # Test initialization with all arguments empty
        with self.assertRaises(ValueError):
            User("", "")

    # Add more test cases as needed for edge cases and additional functionalities

class TestUserDatabase(unittest.TestCase):
    def setUp(self):
        # Initialize a UserDatabase instance for each test case
        self.user_database = UserDatabase()

    def test_add_user(self):
        # Test adding a new user
        self.user_database.add_user("John Doe", "123")
        self.assertEqual(len(self.user_database._users), 1)

        # Test adding a user with empty name
        with self.assertRaises(ValueError):
            self.user_database.add_user("", "123")

        # Test adding a user with empty user ID
        with self.assertRaises(ValueError):
            self.user_database.add_user("John Doe", "")

    # Add more test cases as needed for other functionalities

class TestStorage(unittest.TestCase):
    def setUp(self):
        # Create a temporary folder for testing
        self.test_folder = "test_folder"
        os.makedirs(self.test_folder)

        # Initialize Storage instance
        self.storage = Storage(database_folder=self.test_folder)

    def tearDown(self):
        # Remove the temporary folder and its contents after testing
        for filename in os.listdir(self.test_folder):
            file_path = os.path.join(self.test_folder, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(self.test_folder)

    def test_books_exist(self):
        # Test when books file exists
        with open(os.path.join(self.test_folder, "books.csv"), 'w'):
            pass
        self.assertTrue(self.storage.books_exist())

        # Test when books file does not exist
        self.assertFalse(self.storage.books_exist())

    def test_save_system_state(self):
        # Test saving system state with new books and users
        books = [{"title": "Book1", "author": "Author1", "isbn": "123456"}]
        users = [{"UserID": "user1", "Name": "User 1"}]
        self.storage.save_system_state(books, users)

        # Check if books and users are saved correctly
        self.assertTrue(os.path.exists(os.path.join(self.test_folder, "books.csv")))
        self.assertTrue(os.path.exists(os.path.join(self.test_folder, "users.csv")))

    def test_load_books_data(self):
        # Test loading books data from an existing file
        with open(os.path.join(self.test_folder, "books.csv"), 'w') as f:
            f.write("title,author,isbn\n")
            f.write("Book1,Author1,123456\n")

        books_data = self.storage.load_books_data()
        self.assertEqual(len(books_data), 1)
        self.assertEqual(books_data[0]["title"], "Book1")
        self.assertEqual(books_data[0]["author"], "Author1")
        self.assertEqual(books_data[0]["isbn"], "123456")

        # Test loading books data from a non-existing file
        os.remove(os.path.join(self.test_folder, "books.csv"))
        books_data = self.storage.load_books_data()
        self.assertEqual(len(books_data), 0)

    def test_load_users_data(self):
        # Test loading users data from an existing file
        with open(os.path.join(self.test_folder, "users.csv"), 'w') as f:
            f.write("UserID,Name\n")
            f.write("user1,User 1\n")

        users_data = self.storage.load_users_data()
        self.assertEqual(len(users_data), 1)
        self.assertEqual(users_data[0]["UserID"], "user1")
        self.assertEqual(users_data[0]["Name"], "User 1")

        # Test loading users data from a non-existing file
        os.remove(os.path.join(self.test_folder, "users.csv"))
        users_data = self.storage.load_users_data()
        self.assertEqual(len(users_data), 0)

if __name__ == '__main__':
    unittest.main()
