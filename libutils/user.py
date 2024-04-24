"""Module for managing users in the library."""

from .storage import Storage

class User:
    """Class representing a user in the library."""

    def __init__(self, name: str, user_id: str):
        """
        Initialize a User object.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        self.name = None
        self.user_id = None
        self._storage = Storage()
        self.users_path = self._storage.users_filepath
        existing_users = self._storage.load_data(self.users_path)
        self.existing_ids = [user["UserID"] for user in existing_users]
        
        self.validate_and_set_user_info(name, user_id)

    def validate_and_set_user_info(self, name: str, user_id: str):
        """
        Validate the input information and set user attributes if valid.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        try:
            if not name.strip() or not user_id.strip():
                raise ValueError("User information is incomplete")
            if not isinstance(name, str) or not isinstance(user_id, str):
                raise TypeError("Name and User ID must be strings")
            # Assuming self.existing_ids is a list or set containing existing user IDs
            if user_id in self.existing_ids:
                raise ValueError(f"User ID '{user_id}' already exists in the database")
        except ValueError as ve:
            print("\n❌ Error:", ve," ❌")
        except TypeError as te:
            print("\n❌ Error:", te ," ❌")
        else:
            self.name = name
            self.user_id = user_id


    def __str__(self) -> str:
        """
        Return a string representation of the User object.
        """
        return f"Name: {self.name}, UserID: {self.user_id}"

class UserDatabase:
    """Class for managing user database in the library."""

    def __init__(self):
        """Initialize the UserDatabase."""
        self._users = []
        self._storage = Storage()
    
    def print_users(self, users):
        print("\n-------------------------\nList of users registered in Library 📗:\n-------------------------")
        for _, user_info in enumerate(users, start=1):
            print(f"UserID: {user_info['UserID']}\nName: {user_info['Name']}\nBooksInHand: {user_info['BookInHand']}\n-------------------------")

    def add_user(self, name: str, user_id: str) -> None:
        """
        Add a user to the database.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        try:
            if not name:
                raise ValueError("Name cannot be empty")
            if not user_id:
                raise ValueError("User ID cannot be empty")
            if self._users and str(user_id) in [entry['UserID'] for entry in self.get_users()]:
                raise ValueError("UserID already exists in database.")
            if self._users and int(user_id) in [int(entry['UserID']) for entry in self.get_users()]:
                raise ValueError("UserID already exists in database.")
            if self._storage.users_exist and int(user_id) in [int(entry['UserID']) for entry in self.get_users()]:
                raise ValueError("UserID already exists in database.")
        except ValueError as e:
            if str(e).strip() == "UserID already exists in database.":
                    print(f"\n❌ Error: {e} ❌")
                    self.print_users(self.get_users())
                    
            else:
                print(f"\n❌ Error: {e} ❌")
        else:
            user = User(name, user_id)
            self._users.append(user)
            print("User successfully ✅.")   

    def get_users(self) -> list:
        """
        Retrieve all users from the database.

        Returns:
            list: List of dictionaries containing details of all users in the database.
        """
        user_data = []
        if self._users:
            for user in self._users:
                user_data.append({
                    "Name": user.name,
                    "UserID": user.user_id,
                    "BookInHand": None
                })
        if self._storage.users_exist():
            users_path = self._storage.users_filepath
            loaded_users_data = self._storage.load_data(users_path)
            if loaded_users_data:
                user_data.extend(loaded_users_data)
        
        return user_data

# Global instance of UserDatabase
user_database = UserDatabase()
