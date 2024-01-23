#!/usr/bin/env python3
"""
Module documentation goes here.
"""

from pymongo.collection import Collection

def list_all(mongo_collection: Collection) -> list:
    """
    Lists all documents in the specified MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns:
        list: A list of documents in the collection.
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
