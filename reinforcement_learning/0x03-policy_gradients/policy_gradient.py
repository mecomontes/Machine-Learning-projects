#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 08:20:42 2021

@author: Robinson Montes
"""
import numpy as np


def policy(state, weight):
    """
    Compute policy output with state feature matrices
    and action-feature weights.
    """
    res = state @ weight
    res = np.exp(res)
    return res / res.sum()


def policy_gradient(state, weight):
    """
    Compute policy gradient given state feature matrices
    and action-feature weights.
    """
    state = state.reshape(1, -1)
    policy_value = policy(state, weight)
    random = np.random.random()
    total = 0
    for i, chance in enumerate(policy_value[0]):
        total += chance
        action = i
        if random < total:
            break
    grad = state.T - (policy_value * state.T)

    return action, grad
