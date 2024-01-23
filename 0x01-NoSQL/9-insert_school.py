#!/usr/bin/env python3
"""
9-insert_school module
"""

from pymongo.collection import Collection
from typing import Any

def insert_school(mongo_collection: Collection, **kwargs: Any) -> Any:
    """
    Inserts a new document in the specified MongoDB collection based on kwargs.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.
        **kwargs: Keyword arguments representing the fields for the new document.

    Returns:
        Any: The new _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
