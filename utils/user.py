class User:
    def __init__(self, name: str, user_id: str):
        """
        Initialize a User object.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        self.name = name
        self.user_id = user_id

    def __str__(self) -> str:
        """
        Return a string representation of the User object.
        """
        return f"Name: {self.name}, UserID: {self.user_id}"

class UserDatabase:
    def __init__(self):
        self._users = []

    def add_user(self, name: str, user_id: str) -> None:
        """
        Add a user to the database.

        Args:
            name (str): The name of the user.
            user_id (str): The ID of the user.
        """
        user = User(name, user_id)
        self._users.append(user)

    def get_users(self) -> list:
        """
        Retrieve all users from the database.
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
