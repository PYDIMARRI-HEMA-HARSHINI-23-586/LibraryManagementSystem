class Checkout:
    def __init__(self, user_id: str, isbn: str):
        """
        Initialize a Checkout object.

        Args:
            user_id (str): The ID of the user.
            isbn (str): The ISBN of the book being checked out.
        """
        try:
            if not user_id.strip() and not isbn.strip():
                raise ValueError("User ID and ISBN cannot be empty")
            if not user_id.strip():
                raise ValueError("User ID cannot be empty")
            if not isbn.strip():
                raise ValueError("ISBN cannot be empty")
        except ValueError as e:
            print(f"Error: {e}")
            self.user_id = None
            self.isbn = None
        else:
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
        try:
            if not user_id.strip():
                raise ValueError("User ID cannot be empty")
            if not isbn.strip():
                raise ValueError("ISBN cannot be empty")
        except ValueError as e:
            print(f"Error: {e}")
        else:
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
