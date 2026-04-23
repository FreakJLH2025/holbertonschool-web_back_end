#!/usr/bin/env python3
"""
Module 11-schools_by_topic
Defines a function to find schools by topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    Return the list of schools having a specific topic.

    Args:
        mongo_collection: pymongo collection object
        topic (str): topic searched

    Returns:
        List of documents that contain the topic
    """
    return list(mongo_collection.find({"topics": topic}))
