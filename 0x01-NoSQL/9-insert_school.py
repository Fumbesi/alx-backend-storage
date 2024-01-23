#!/usr/bin/env python3
"""Python function that inserts a new document in a collection based on kwargs"""

from pymongo.collection import Collection

def insert_school(mongo_collection: Collection, **kwargs) -> str:
    """
    Inserts a new document in the MongoDB collection based on the provided kwargs.

    :param mongo_collection: The `mongo_collection` parameter is expected
    to be a MongoDB collection object.
    It represents a collection of documents in a MongoDB database.
    :param kwargs: Key-value pairs representing the fields and values of the new document.
    :return: The new _id of the inserted document.
    """
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    return str(result.inserted_id)
