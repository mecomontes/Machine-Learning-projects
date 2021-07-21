#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 08:20:02 2021

@author: Robinson Montes
"""
import pandas as pd


def from_numpy(array):
    """
    creates a pd.DataFrame from a np.ndarray
    param array: np.ndarray
    return: the newly created pd.DataFrame
    """
    col = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    col_fit = col[:array.shape[1]]
    return pd.DataFrame(array, columns=col_fit)
