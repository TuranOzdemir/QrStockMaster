import firebase_admin
from typing import Optional
from datetime import datetime
from dataclasses import dataclass
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter

import logging

# logging.basicConfig(level = logging.INFO)

@dataclass
class User:
    """
    Dataclass representing a user with its attributes.
    """
    first_name: str
    last_name: str
    email: str
    password: str
    date_created: datetime


@dataclass
class Product:
    """
    Dataclass representing a product with its attributes.
    """
    product_name: str
    description: str
    stock: int
    owner_id: str
    date_created: datetime
    date_updated: Optional[datetime]


class DatabaseManager:
    """
    Database manager class for interacting with the Firebase database.
    """

    def __init__(self, db):
        self.db = db

    def add_user(self, user: User):
        """
        Adds a new user to the database.

        Args:
            user: The user object to be added.

        Returns:
            The ID of the newly created user document.
        """
        try:
            user_ref, user_id = self.db.collection("users").add({
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "password": user.password,
                "date_created": user.date_created
            })
            logging.info("Successfully added user: %s", user_id.id)
        except Exception as e:
            logging.error("Error adding user: %s", e)
            raise e

        # Create a reference to the user document
        user_doc_ref = self.db.collection("users").document(user_id.id)

        # Add products subcollection inside the user document
        products_subcollection_ref = user_doc_ref.collection("products")

        return user_id

    def add_product(self, user_id: str, product: Product):
        """
        Adds a new product to a user's product collection.

        Args:
            user_id: The ID of the user that owns the product.
            product: The product object to be added.

        Returns:
            The ID of the newly created product document.
        """
        try:
            product_ref, product_id = self.db.collection("users").document(
                user_id).collection("products").add({
                    "product_name": product.product_name,
                    "description": product.description,
                    "stock": product.stock,
                    "owner_id": product.owner_id,
                    "date_created": product.date_created,
                    "date_updated": product.date_updated,
                })
            logging.info("Successfully added product: %s", product_id.id)
        except Exception as e:
            logging.error("Error adding product: %s", e)
            raise e

        return product_id

    def get_user_products(self, user_id: str):
        """
        Gets all products for a specific user.

        Args:
            user_id: The ID of the user whose products to retrieve.

        Returns:
            A list of dictionaries representing the user's products,
            or None if no products are found.
        """
        try:
            products_ref = self.db.collection("users").document(
                user_id).collection("products").get()
            user_products = [doc.to_dict() for doc in products_ref]
            logging.info("Retrieved %s products for user: %s", len(user_products), user_id)
            return user_products if user_products else None
        except Exception as e:
            logging.error("Error retrieving user products: %s", e)
            raise e

    def get_user_id(self, email: str):
        """
        Gets the user ID for a given email address.

        Args:
            email: The email address of the user.

        Returns:
            The ID of the user document, or None if no user is found.
        """
        try:
            query = self.db.collection('users').where(filter = 
                FieldFilter("email", "==", email))
            found_user = next(query.stream(), None)  # Check for available documents

            if found_user:
                user_id = found_user.id
                logging.info("Found user ID: %s for email: %s", user_id, email)
                return user_id
            else:
                logging.info("No user found with email: %s", email)
                return None
        except Exception as e:
            logging.error("Error retrieving user ID for email: %s", email, exc_info=True)
            raise e

    



