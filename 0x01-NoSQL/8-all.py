#!/usr/bin/env python3
"""
This module defines a function to list all documents in a MongoDB collection.
"""

from pymongo.collection import Collection
from typing import List, Dict, Any

def list_all(mongo_collection: Collection) -> List[Dict[str, Any]]:
    """
    Lists all documents in the specified MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns:
        List[Dict[str, Any]]: A list of documents in the collection. Returns an empty list if no documents are present.
    """
    documents = list(mongo_collection.find())
    return documents

if __name__ == "__main__":
    # Example usage
    from pymongo import MongoClient

    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    schools = list_all(school_collection)

    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
