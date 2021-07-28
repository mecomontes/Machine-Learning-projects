#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 06:10:33 2021

@author: Robinson Montes
"""


def list_all(mongo_collection):
    """
    lists all documents in a collection:
    :param mongo_collection: pymongo collection object
    :return: empty list if no document in the collection
    """
    documents = []
    collection = mongo_collection.find()
    for doc in collection:
        documents.append(doc)
    return documents
