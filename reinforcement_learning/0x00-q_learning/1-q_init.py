#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 08:00:42 2021

@author: Robinson Montes
"""
import numpy as np


def q_init(env):
    """
    initializes the Q-table
    :param env: the FrozenLakeEnv instance
    :return: Q-table as a numpy.ndarray of zeros
    """
    Q = np.zeros((env.observation_space.n, env.action_space.n))

    return Q
