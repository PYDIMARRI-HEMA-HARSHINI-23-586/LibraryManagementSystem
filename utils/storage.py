import csv
from typing import List, Dict
from datetime import datetime
import os

class Storage:
    TIMESTAMP_FIELDNAME = "timestamp"
    BOOKS_FILENAME = "books.csv"
    USER_INFO = "users.csv"

    def __init__(self, database_folder="database"):
        """
        Initialize the Storage class.

        Args:
            database_folder (str, optional): The folder where database files will be stored. Defaults to "database".
        """
        self.database_folder = database_folder
        self.books_filepath = os.path.join(self.database_folder, self.BOOKS_FILENAME)
        self.users_filepath = os.path.join(self.database_folder, self.USER_INFO)

        # Create the database folder if it doesn't exist
        if not os.path.exists(self.database_folder):
            os.makedirs(self.database_folder)
    
    def books_exist(self) -> bool:
        """
        Check if the books.csv file exists in the database folder.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.isfile(self.books_filepath)

            
    def save_system_state(self, books: List[Dict], users: List[Dict]) -> None:
        """
        Save the current state of the library management system in CSV format.

        Args:
            books (List[Dict]): List of dictionaries representing books.
            users (List[Dict]): List of dictionaries representing users.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if books:
            existing_books = self.load_books_data()
            existing_isbns = set(book["isbn"] for book in existing_books)
            new_books = [book for book in books if book["isbn"] not in existing_isbns] 
            if new_books:
                with open(self.books_filepath, 'a', newline='') as books_file:
                    fieldnames = list(new_books[0].keys()) + [self.TIMESTAMP_FIELDNAME]
                    books_writer = csv.DictWriter(books_file, fieldnames=fieldnames)
                    if os.path.getsize(self.books_filepath) == 0:
                        books_writer.writeheader()
                    for book in new_books:
                        book[self.TIMESTAMP_FIELDNAME] = current_time
                        books_writer.writerow(book)
        
        if users:
            existing_users = self.load_users_data()
            existing_ids = set(user["UserID"] for user in existing_users)
            new_users = [user for user in users if user["UserID"] not in existing_ids] 
            if new_users:
                with open(self.users_filepath, 'a', newline='') as users_file:
                    fieldnames = list(new_users[0].keys()) + [self.TIMESTAMP_FIELDNAME]
                    users_writer = csv.DictWriter(users_file, fieldnames=fieldnames)
                    if os.path.getsize(self.users_filepath) == 0:
                        users_writer.writeheader()
                    for user in new_users:
                        user[self.TIMESTAMP_FIELDNAME] = current_time
                        users_writer.writerow(user)

    def load_books_data(self) -> List[Dict]:
        """
        Load books data from a CSV file.

        Returns:
            List[Dict]: The loaded books data.
        """
        books_data = []
        if os.path.exists(self.books_filepath):
            with open(self.books_filepath, 'r', newline='') as books_file:
                books_reader = csv.DictReader(books_file)
                for row in books_reader:
                    books_data.append(dict(row))
        return books_data

    def load_users_data(self) -> List[Dict]:
        """
        Load users data from a CSV file.

        Returns:
            List[Dict]: The loaded users data.
        """
        users_data = []
        if os.path.exists(self.users_filepath):
            with open(self.users_filepath, 'r', newline='') as users_file:
                users_reader = csv.DictReader(users_file)
                for row in users_reader:
                    users_data.append(dict(row))
        return users_data
