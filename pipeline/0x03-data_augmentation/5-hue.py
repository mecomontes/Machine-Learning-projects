#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 8:10:33 2021

@author: Robinson Montes
"""
import tensorflow as tf


def change_hue(image, delta):
    """
    changes the hue of an image
    :param image: 3D tf.Tensor containing the image to change
    :param delta: the amount the hue should change
    :return: the altered image
    """
    img = tf.image.adjust_hue(image, delta)
    return img
