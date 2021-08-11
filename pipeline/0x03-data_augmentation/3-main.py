#!/usr/bin/env python3

import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
import os
shear_image = __import__('3-shear').shear_image

tf.compat.v1.enable_eager_execution()
tf.compat.v1.set_random_seed(3)

doggies = tfds.load('stanford_dogs', split='train', as_supervised=True)
for image, _ in doggies.shuffle(10).take(1):
    fig = plt.figure(figsize=(4, 4), facecolor="w")
    plt.imshow(shear_image(image, 50))
    plt.show()

    # save as png
    outfile = os.path.join('images', '3-main' + ".png")

    fig.savefig(outfile, dpi=150)
