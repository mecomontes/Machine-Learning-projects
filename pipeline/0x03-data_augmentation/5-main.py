#!/usr/bin/env python3

import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import os

change_hue = __import__('5-hue').change_hue

tf.compat.v1.enable_eager_execution()
tf.compat.v1.set_random_seed(5)

doggies = tfds.load('stanford_dogs', split='train', as_supervised=True)
for image, _ in doggies.shuffle(10).take(1):
    fig = plt.figure(figsize=(4, 4), facecolor="w")
    plt.imshow(change_hue(image, -0.5))
    plt.show()

    # save as png
    outfile = os.path.join('images', '5-main' + ".png")

    fig.savefig(outfile, dpi=150)
