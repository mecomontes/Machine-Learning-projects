#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 08:00:42 2021

@author: Robinson Montes
"""
import numpy as np


def epsilon_greedy(Q, state, epsilon):
    """
    uses epsilon-greedy to determine the next action
    :param Q: numpy.ndarray containing the q-table
    :param state: current state
    :param epsilon: epsilon to use for the calculation
    :return: next action index
    """
    pos_action = Q.shape[1]

    if np.random.uniform(0, 1) < epsilon:
        # Explore: select a random action
        action_index = np.random.randint(pos_action)
    else:
        # Exploit: select the action with max value (future reward)
        action_index = np.argmax(Q[state])

    return action_index
