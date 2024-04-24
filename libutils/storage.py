"""Module for managing storage of data in the library."""

import csv
from typing import List, Dict
from datetime import datetime
import os

class Storage:
    """A class to manage data storage for a library management system using CSV files."""

    def __init__(self, database_folder: str = "database") -> None:
        """
        Initialize the Storage class.

        Args:
            database_folder (str, optional): The folder where database files will be stored. Defaults to "database".
        """
        self.database_folder = database_folder
        self.books_filepath = os.path.join(self.database_folder, "books.csv")
        self.users_filepath = os.path.join(self.database_folder, "users.csv")

        # Create the database folder if it doesn't exist
        if not os.path.exists(self.database_folder):
            os.makedirs(self.database_folder)

    def save_system_state(self, books: List[Dict[str, str]], users: List[Dict[str, str]]) -> None:
        """
        Save the current state of the library management system in CSV format.

        Args:
            books (List[Dict[str, str]]): List of dictionaries representing books.
            users (List[Dict[str, str]]): List of dictionaries representing users.
        """
        
        if books:
            self.save_data(books, self.books_filepath, self._get_books_fieldnames(), "isbn")
        
        if users:
            self.save_data(users, self.users_filepath, self._get_users_fieldnames(), "UserID")

    def save_data(self, data: List[Dict[str, str]], filepath: str, fieldnames: List[str], unique_key: str, mode = 'a') -> None:
        """
        Save data to a CSV file.

        Args:
            data (List[Dict[str, str]]): List of dictionaries representing data.
            filepath (str): Path to the CSV file.
            fieldnames (List[str]): Field names for the CSV file.
            unique_key (str): Unique key to check for duplicates.
            current_time (str): Current timestamp.
        """
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        existing_data = self.load_data(filepath)
        if unique_key:
            
            existing_keys = set(record[unique_key] for record in existing_data)
            new_records = []

            for record in data:
                if record[unique_key] not in existing_keys:
                    # record = self._fill_empty_values(record,custom_value)
                    if unique_key == "UserID":
                        record['BookInHand'] = None
                    else:
                        record["AvailableInLibrary"] = "Yes"

                    record['timestamp'] = current_time
                    new_records.append(record)
            if new_records:
                with open(filepath, mode, newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    if os.path.getsize(filepath) == 0:
                        writer.writeheader()
                    writer.writerows(new_records)
                print(f"\nUpdated {filepath} Successfully ✅\n")
                return True
            

        else:
            fieldnames = list(data[0].keys())

            with open(filepath, mode, newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
            with open(filepath, mode, newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                if os.path.getsize(filepath) == 0:
                    writer.writeheader()
                    for record in data:
                        record['timestamp'] = current_time
                        writer.writerow(record)
            return True

    def load_data(self, filepath: str) -> List[Dict[str, str]]:
        """
        Load data from a CSV file.

        Args:
            filepath (str): Path to the CSV file.

        Returns:
            List[Dict[str, str]]: The loaded data.
        """
        data = []
        if os.path.exists(filepath):
            with open(filepath, 'r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data.append(dict(row))
        # else:
        #     print("\n------------------------------------------------\n⚠️ No Users in the library, Please add users ⚠️\n------------------------------------------------")
        return data
    
    def _fill_empty_values(self, record: Dict[str, str], custom_value: str) -> Dict[str, str]:
        """
        Fill empty values in a record with custom value.

        Args:
            record (Dict[str, str]): The record to fill.

        Returns:
            Dict[str, str]: The record with empty values filled with None.
        """
        # breakpoint()
        return {key: value if value.strip() else custom_value for key, value in record.items()}

    def _get_books_fieldnames(self) -> List[str]:
        """Get the field names for the books CSV file."""
        return ["title", "author", "isbn", "AvailableInLibrary", "timestamp"]

    def _get_users_fieldnames(self) -> List[str]:
        """Get the field names for the users CSV file."""
        return ["Name", "UserID", "BookInHand", "timestamp"]

    def books_exist(self) -> bool:
        """
        Check if the books.csv file exists in the database folder.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.isfile(self.books_filepath)
    
    def users_exist(self) -> bool:
        """
        Check if the users.csv file exists in the database folder.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.isfile(self.users_filepath)
