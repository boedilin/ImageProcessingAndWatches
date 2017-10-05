"""
=================
An animated image
=================

This example demonstrates how to animate an image.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
data = np.load('test.npy')
counter = 0


def f():
    global counter
    counter += 1
    return data[counter]["sad"]


# imshow(array)
im = plt.imshow(f(), animated=True)


def updatefig(*args):
    im.set_array(f())
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=50, blit=True)
plt.show()