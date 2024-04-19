"""Module for managing checkouts in the library."""

from utils.check import checkout_database

class CheckoutManagement:
    """Class for managing checkouts in the library."""
    
    def checkout_book(self, user_id: str, isbn: str) -> None:
        """
        Checkout a book for a user.

        Args:
            user_id (str): The ID of the user.
            isbn (str): The ISBN of the book to checkout.
        """
        checkout_database.checkout_book(user_id, isbn)
