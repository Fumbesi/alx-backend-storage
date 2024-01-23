#!/usr/bin/env python3
"""
Lists all documents in a MongoDB collection.
"""

from pymongo.collection import Collection
from typing import List

def list_all(mongo_collection: Collection) -> List[dict]:
    """
    Lists all documents in the MongoDB collection.

    Args:
        mongo_collection (Collection): The pymongo collection object.

    Returns:
        List[dict]: A list containing all documents in the collection.
    """
    return list(mongo_collection.find())

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {}".format(school.get('_id'), school.get('name')))
