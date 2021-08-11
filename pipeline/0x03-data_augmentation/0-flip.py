#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 8:10:33 2021

@author: Robinson Montes
"""
import tensorflow as tf


def flip_image(image):
    """
    flips an image horizontally
    :param image: 3D tf.Tensor containing the image to flip
    :return: flipped image
    """
    flip = tf.image.flip_left_right(image)
    return flip
