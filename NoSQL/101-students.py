#!/usr/bin/env python3
"""   function that returns all students by order of points   """
import pymongo


def top_students(mongo_collection):
    pipeline = [
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$scores"
                }
            }
        },
        {"$sort": {"averageScore": -1}}
    ]

    return list(mongo_collection.aggregate(pipeline))