#!/usr/bin/env python3
"""
Define Python function that changes all topics of a school document based on the name
"""

from pymongo.collection import Collection

def update_topics(mongo_collection: Collection, name: str, topics: list):
    """
    The function `update_topics` changes all topics of a school document based on the name.

    :param mongo_collection: The `mongo_collection` parameter is the
    collection in the MongoDB database where you want to update the
    school document.
    :param name: The `name` parameter is the school name to update.
    :param topics: The `topics` parameter is a list of strings representing
    the list of topics approached in the school.
    """
    mongo_collection.update_many(
        {'name': name},
        {'$set': {'topics': topics}}
    )

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    school_collection = client.my_db.school

    update_topics(school_collection, "Holberton school", ["Sys admin", "AI", "Algorithm"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))

    update_topics(school_collection, "Holberton school", ["iOS"])

    schools = list_all(school_collection)
    for school in schools:
        print("[{}] {} {}".format(school.get('_id'), school.get('name'), school.get('topics', "")))
