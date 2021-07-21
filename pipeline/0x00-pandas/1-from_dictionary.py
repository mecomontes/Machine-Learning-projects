#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 08:20:02 2021

@author: Robinson Montes
"""
import numpy as np
import pandas as pd


init_dict = {'First': [0.0, 0.5, 1.0, 1.5],
             'Second': ['one', 'two', 'three', 'four']}
index = list('ABCD')
df = pd.DataFrame(init_dict, index=index)
