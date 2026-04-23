#!/usr/bin/env python3
"""
Module 8-all
Defines a function to list all documents in a MongoDB collection
"""


def list_all(mongo_collection):
    """
    List all documents in a collection.

    Args:
        mongo_collection: pymongo collection object

    Returns:
        List of documents in the collection, or an empty list if none exist
    """
    return [doc for doc in mongo_collection.find()]
