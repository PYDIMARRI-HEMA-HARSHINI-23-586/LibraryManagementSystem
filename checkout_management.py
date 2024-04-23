"""Module for managing checkouts in the library."""

from libutils.check import checkout_database

class CheckoutManagement:
    """
    Class for managing checkouts in the library.
    """
    
    def checkout_book(self) -> None:
        """
        Checkout a book for a user.

        Args:
            user_id (str): The ID of the user.
            isbn (str): The ISBN of the book to check out.
        """
        checkout_database.checkout_book()
