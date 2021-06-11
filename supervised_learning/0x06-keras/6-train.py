#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 11:00:22 2021

@author: Robinson Montes
"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size, epochs,
                validation_data=None, early_stopping=False, patience=0,
                verbose=True, shuffle=False):
    """
    Function that trains a model using mini-batch gradient descent:
    Arguments:
     - network is the model to train
     - data is a numpy.ndarray of shape (m, nx) containing the input data
     - labels is a one-hot numpy.ndarray of shape (m, classes) containing
        the labels of data
     - batch_size is the size of the batch used for mini-batch gradient descent
     - epochs is the number of passes through data for mini-batch
        gradient descent
     - verbose is a boolean that determines if output should be printed
        during training
     - shuffle is a boolean that determines whether to shuffle the batches
        every epoch.
     - validation_data is the data to validate the model with, if not None
     - early_stopping is a boolean that indicates whether early stopping
        should be used
        * should only be performed if validation_data exists
        * should be based on validation loss
     - patience is the patience used for early stopping

    Returns:
     The History object generated after training the model
    """
    callback = []
    if validation_data:
        early_stop = K.callbacks.EarlyStopping(monitor='val_loss',
                                               patience=patience)
        callback.append(early_stop)
    history = network.fit(x=data, y=labels, epochs=epochs,
                          batch_size=batch_size,
                          validation_data=validation_data,
                          shuffle=shuffle, verbose=verbose,
                          callbacks=callback)

    return history
