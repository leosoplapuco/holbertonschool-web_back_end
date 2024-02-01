#!/usr/bin/env python3
"""   pymongo database   """


def update_topics(mongo_collection, name, topics):
    """   Changing all topics of a school document based on a specific name   """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})