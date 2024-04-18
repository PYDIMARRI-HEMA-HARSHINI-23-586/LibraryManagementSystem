class Checkout:
    def __init__(self, user_id: str, isbn: str):
        """
        Initialize a Checkout object.

        Args:
            user_id (str): The ID of the user.
            isbn (str): The ISBN of the book being checked out.
        """
        self.user_id = user_id
        self.isbn = isbn

class CheckoutDatabase:
    def __init__(self):
        self._checkouts = []

    def checkout_book(self, user_id: str, isbn: str) -> None:
        """
        Record a book checkout in the database.

        Args:
            user_id (str): The ID of the user checking out the book.
            isbn (str): The ISBN of the book being checked out.
        """
        checkout = Checkout(user_id, isbn)
        self._checkouts.append(checkout)

    def get_checkouts(self) -> list:
        """
        Retrieve all book checkouts from the database.

        Returns:
            list: List of Checkout objects representing book checkouts.
        """
        return self._checkouts

# Global instance of CheckoutDatabase
checkout_database = CheckoutDatabase()
