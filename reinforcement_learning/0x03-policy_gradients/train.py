#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 08:20:42 2021

@author: Robinson Montes
"""
from policy_gradient import policy_gradient
import numpy as np


def train(env, nb_episodes, alpha=0.00045, gamma=0.98, show_result=False):
    """Train a policy based Monte Carlo/REINFORCE algorithm"""
    scores = []
    weights = np.random.rand(env.observation_space.shape[0],
                             env.action_space.n)
    for episode in range(nb_episodes):
        state = env.reset()[None, :]

        grads = []
        rewards = []
        actions = []
        done = 0
        while not done:
            if show_result and not episode % 1000:
                env.render()
            action, grad = policy_gradient(state, weights)
            # print("step", action, grad)
            state, reward, done, info = env.step(action)
            grads.append(grad)
            rewards.append(reward)
            actions.append(action)
        total_reward = 0
        """
        if not episode %100 and 0:
            print("weights", weights)
        """
        for grad, reward, action in zip(grads[::-1], rewards[::-1],
                                        actions[::-1]):
            total_reward = reward + total_reward * gamma
            weights[:, action] += alpha * grad[:, action] * total_reward
            """
            if not episode % 100 and 0:
                # print(total_reward, grad)
                # print(alpha * grad * total_reward)
            """
        scores.append(sum(rewards))
        print(episode, sum(rewards))
        """
        if not episode % 100:
            print(episode, sum(rewards))
            #print("grads", len(grads), grads)
            #print("rewards", len(rewards), rewards[::-1])
            #print(weights)
        """
    return scores
