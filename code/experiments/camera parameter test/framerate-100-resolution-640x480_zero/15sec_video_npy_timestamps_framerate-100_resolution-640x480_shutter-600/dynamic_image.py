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
data = np.load('motion_vectors_resolution-640x480_framerate-30_shutter-12000.npy')
counter = 0


def f():
    global counter
    counter += 1
    if (data.shape[0]-1) != counter:
        return data[counter]["sad"]
    else:
        ani.event_source.stop()


# imshow(array)
im = plt.imshow(f(), animated=True)


def updatefig(*args):
    im.set_array(f())
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=20, blit=True)
plt.show()