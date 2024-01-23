#!/usr/bin/env python3
"""
8-all module
"""

from pymongo.collection import Collection
from typing import List

def list_all(mongo_collection: Collection) -> List[dict]:
    """
    Lists all documents in the specified MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns:
        list: A list of documents in the collection. Returns an empty list if no documents.
    """
    documents = list(mongo_collection.find())
    return documents
