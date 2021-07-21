#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 08:20:02 2021

@author: Robinson Montes
"""
import pandas as pd


def from_file(filename, delimiter):
    """
    loads data from a file as a pd.DataFrame
    :param filename: file to load from
    :param delimiter: the column separator
    :return: the loaded pd.DataFrame
    """
    return pd.read_csv(filename, sep=delimiter)
