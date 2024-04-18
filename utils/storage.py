import csv
from typing import List, Dict
from datetime import datetime
import os

class Storage:
    TIMESTAMP_FIELDNAME = "timestamp"
    def __init__(self, database_folder="database"):
        self.database_folder = database_folder

        # Create the database folder if it doesn't exist
        if not os.path.exists(self.database_folder):
            os.makedirs(self.database_folder)
            
    def save_system_state(self, books: List[Dict], users: List[Dict], books_filename: str = "books.csv", users_filename: str = "users.csv") -> None:
        """
        Save the current state of the library management system in CSV format.

        Args:
            books (List[Dict]): List of dictionaries representing books.
            users (List[Dict]): List of dictionaries representing users.
            books_filename (str, optional): The name of the file to save the books data to. Defaults to "books.csv".
            users_filename (str, optional): The name of the file to save the users data to. Defaults to "users.csv".
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if books:
            # Save books data
            books_filepath = os.path.join(self.database_folder, books_filename)
            with open(books_filepath, 'a', newline='') as books_file:
                fieldnames = list(books[0].keys()) + [self.TIMESTAMP_FIELDNAME]  # Add timestamp fieldname
                books_writer = csv.DictWriter(books_file, fieldnames=fieldnames)
                if books_file.tell() == 0:  # Check if the file is empty
                    books_writer.writeheader()
                for book in books:
                    book[self.TIMESTAMP_FIELDNAME] = current_time
                    books_writer.writerow(book)
        
        if users:
            # Save users data
            users_filepath = os.path.join(self.database_folder, users_filename)
            with open(users_filepath, 'a', newline='') as users_file:
                fieldnames = list(users[0].keys()) + [self.TIMESTAMP_FIELDNAME]  # Add timestamp fieldname
                users_writer = csv.DictWriter(users_file, fieldnames=fieldnames)
                if users_file.tell() == 0:  # Check if the file is empty
                    users_writer.writeheader()
                for user in users:
                    user[self.TIMESTAMP_FIELDNAME] = current_time
                    users_writer.writerow(user)

    def load_books_data(self, filename: str) -> List[Dict]:
        """
        Load books data from a CSV file.

        Args:
            filename (str): The name of the file to load books data from.

        Returns:
            List[Dict]: The loaded books data.
        """
        books_data = []
        with open(filename, 'r', newline='') as books_file:
            books_reader = csv.DictReader(books_file)
            for row in books_reader:
                books_data.append(dict(row))
        return books_data


    def load_users_data(self, filename: str) -> List[Dict]:
        """
        Load users data from a CSV file.

        Args:
            filename (str): The name of the file to load users data from.

        Returns:
            List[Dict]: The loaded users data.
        """
        users_data = []
        with open(filename, 'r', newline='') as users_file:
            users_reader = csv.DictReader(users_file)
            for row in users_reader:
                users_data.append(dict(row))
        return users_data
