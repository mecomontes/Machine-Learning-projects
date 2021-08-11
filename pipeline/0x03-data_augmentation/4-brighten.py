#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 8:10:33 2021

@author: Robinson Montes
"""
import tensorflow as tf


def change_brightness(image, max_delta):
    """
    randomly changes the brightness of an image
    :param image: 3D tf.Tensor containing the image to change
    :param max_delta: maximum amount the image should be brightened
    :return: the altered image
    """
    img = tf.image.adjust_brightness(image, max_delta)
    return img
