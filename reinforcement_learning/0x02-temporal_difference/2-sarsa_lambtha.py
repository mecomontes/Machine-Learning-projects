#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 5 08:00:42 2021

@author: Robinson Montes
"""
import numpy as np


def sarsa_lambtha(env, Q, lambtha, episodes=5000, max_steps=100,
                  alpha=0.1, gamma=.99, epsilon=1, min_epsilon=0.1,
                  epsilon_decay=0.05):
    """Train TD(Lambda) value estimation on a OpenAI gym"""
    success = 0
    for episode in range(episodes):
        actions = env.action_space.n
        eligibility = np.zeros(Q.shape)
        prev_state = env.reset()
        n = np.random.ranf()
        if n > epsilon:
            action = np.random.randint(0, actions)
        else:
            action = np.argmax(Q[prev_state])
        for step in range(max_steps):
            state = state, reward, done, info = env.step(action)
            epsilon *= 1 - epsilon_decay
            if epsilon < min_epsilon:
                epsilon = min_epsilon
            eligibility *= gamma * lambtha
            eligibility[prev_state, action] += 1
            prev_action = action
            n = np.random.ranf()
            if n > epsilon:
                action = np.random.randint(0, actions)
            else:
                action = np.argmax(Q[state])

            if done:
                Q[prev_state, prev_action] = (Q[prev_state, prev_action]
                                              + alpha * (reward
                                                         - Q[prev_state,
                                                             prev_action]))
                break
            Q[prev_state, prev_action] = (Q[prev_state, prev_action]
                                          + alpha * (reward + Q[state, action]
                                             - Q[prev_state, prev_action]))

            prev_state = state

            if done:
                break
    return Q
