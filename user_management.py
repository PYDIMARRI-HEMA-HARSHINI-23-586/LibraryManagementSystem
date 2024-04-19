"""
Module for user management functionalities.
"""

from utils.user import user_database

class UserManagement:
    """
    Class for managing users in the system.
    """
    
    def add_user(self, name: str, user_id: str) -> None:
        """
        Add a user to the system.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        user_database.add_user(name, user_id)

    def list_users(self) -> None:
        """
        List all users in the system.
        """
        return user_database.get_users()
