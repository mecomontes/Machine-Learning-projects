#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 06:10:33 2021

@author: Robinson Montes
"""


def schools_by_topic(mongo_collection, topic):
    """
    :param mongo_collection: the pymongo collection object
    :param topic: topic searched
    :return: the list of school having a specific topic
    """
    match = []
    results = mongo_collection.find({"topics": {"$all": [topic]}})
    for result in results:
        match.append(result)
    return match
