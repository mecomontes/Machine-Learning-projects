#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 06:10:33 2021

@author: Robinson Montes
"""


def update_topics(mongo_collection, name, topics):
    """ function that changes all topics of a school document based
        on the name
        mongo_collection will be the pymongo collection object
        name (string) will be the school name to update
        topics (list of strings) will be the list of topics approached
            in the school
    """

    newvalues = {"$set": {"topics": topics}}
    mongo_collection.update_many({"name": name}, newvalues)
