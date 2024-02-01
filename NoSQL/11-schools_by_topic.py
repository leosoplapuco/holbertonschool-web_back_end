#!/usr/bin/env python3
"""   pymongo database   """


def schools_by_topic(mongo_collection, topic):
    """   Returing the list of school having a specific topic   """
    return mongo_collection.find({"topics": topic})