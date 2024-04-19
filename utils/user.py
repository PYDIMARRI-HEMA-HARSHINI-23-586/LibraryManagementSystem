"""Module for managing users in the library."""

class User:
    """Class representing a user in the library."""

    def __init__(self, name: str, user_id: str):
        """
        Initialize a User object.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        try:
            if not name:
                raise ValueError("Name cannot be empty")
            if not user_id:
                raise ValueError("User ID cannot be empty")
        except ValueError as e:
            print(f"Error: {e}")
            self.name = None
            self.user_id = None
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
        except ValueError as e:
            print(f"Error: {e}")
        else:
            user = User(name, user_id)
            self._users.append(user)

    def get_users(self) -> list:
        """
        Retrieve all users from the database.

        Returns:
            list: List of dictionaries containing details of all users in the database.
        """
        user_data = []
        for user in self._users:
            user_data.append({
                "Name": user.name,
                "UserID": user.user_id
            })
        return user_data

# Global instance of UserDatabase
user_database = UserDatabase()
