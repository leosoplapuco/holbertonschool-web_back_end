#!/usr/bin/env python3
"""   pymongo database   """


def insert_school(mongo_collection, **kwargs):
    """   inserting a new document in a database of mongo   """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id