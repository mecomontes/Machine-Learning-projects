#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 08:00:42 2021

@author: Robinson Montes
"""

import gym
from rl.agents.dqn import DQNAgent
from rl.memory import SequentialMemory
import keras as K

create_q_model = __import__('train').create_q_model
AtariProcessor = __import__('train').AtariProcessor


if __name__ == '__main__':
    env = gym.make("Breakout-v0")
    env.reset()
    num_actions = env.action_space.n
    window = 4  # number of screenshots

    # CREATE MODEL
    # deep convolutional neural network model
    model = create_q_model(num_actions, window)
    memory = SequentialMemory(limit=1000000, window_length=window)
    processor = AtariProcessor()

    dqn = DQNAgent(model=model,
                   nb_actions=num_actions,
                   processor=processor,
                   memory=memory)

    dqn.compile(K.optimizers.Adam(lr=.00025), metrics=['mae'])

    # load weights.
    dqn.load_weights('policy.h5')

    # evaluate algorithm for 10 episodes.
    dqn.test(env, nb_episodes=10, visualize=True)
