#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 8:10:33 2021

@author: Robinson Montes
"""
import tensorflow as tf


def shear_image(image, intensity):
    """
    randomly shears an image
    :param image: 3D tf.Tensor containing the image to shear
    :param intensity: the intensity with which the image should be sheared
    :return: the sheared image
    """
    img = tf.keras.preprocessing.image.img_to_array(image)
    sheared_img = tf.keras.preprocessing.image.random_shear(img, intensity,
                                                            row_axis=0,
                                                            col_axis=1,
                                                            channel_axis=2
                                                            )
    image_out = tf.keras.preprocessing.image.array_to_img(sheared_img)
    return image_out
