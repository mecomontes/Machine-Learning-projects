#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 08:20:02 2021

@author: Robinson Montes
"""
import pandas as pd


from_file = __import__('2-from_file').from_file
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
stats = df.describe().drop(["Timestamp"], axis=1)
print(stats)
