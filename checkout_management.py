from utils.check import checkout_database

class CheckoutManagement:
    def checkout_book(self, user_id: str, isbn: str) -> None:
        """
        Checkout a book for a user.

        Args:
            user_id (str): The ID of the user.
            isbn (str): The ISBN of the book to checkout.
        """
        checkout_database.checkout_book(user_id, isbn)
