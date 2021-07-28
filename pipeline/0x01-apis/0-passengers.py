#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 08:20:02 2021

@author: Robinson Montes
"""
import requests


def availableShips(passengerCount):
    """
    list of ships that can hold a
         given number of passengers
    :param passengerCount: number of passengers
    :return: list of ships
    """
    url = "https://swapi-api.hbtn.io/api/starships/"
    ships = []

    while url is not None:
        r = requests.get(url)
        results = r.json()["results"]
        for ship in results:
            p = ship["passengers"]
            p = p.replace(',', '')
            if p.isnumeric() and int(p) >= passengerCount:
                ships.append(ship["name"])
        url = r.json()["next"]
    return ships
