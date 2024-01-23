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

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school
    new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
    print("New school created: {}".format(new_school_id))

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('address', "")))
