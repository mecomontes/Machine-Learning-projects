#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 06:10:33 2021

@author: Robinson Montes
"""


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs:
        mongo_collection will be the pymongo collection object
        Returns the new _id
    """
    id_ = mongo_collection.insert_one(kwargs).inserted_id
    return id_
