#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 8 08:32:21 2021

@author: Robinson Montes
"""


cases = ['exit', 'goodbye', 'bye']
"""
Create the loop
Script that takes in input from the user with the prompt Q:
and prints A: as a response.
If the user inputs exit, quit, goodbye, or bye, case insensitive,
print A: Goodbye and exit
"""
while True:
    ans = input('Q: ')
    ans = ans.lower()

    if ans in cases:
        print('A: Goodbye')
        exit(0)
    else:
        print('A: ')
