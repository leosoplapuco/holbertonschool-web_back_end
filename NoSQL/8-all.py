#!/usr/bin/env python3
"""   list all pymongodb   """


def list_all(mongo_collection):
    """   lists all documents in a collectio   """
    documents = mongo_collection.find()
    return documents