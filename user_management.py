from utils.user import user_database

class UserManager:
    def add_user(self, name: str, user_id: str) -> None:
        """
        Add a user to the system.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        user_database.add_user(name, user_id)
