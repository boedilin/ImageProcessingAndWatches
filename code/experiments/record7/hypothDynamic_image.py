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
data = np.load('myTest.npy')
counter = 0

def f():
    global counter
    counter += 1
    if (data.shape[0]-1) != counter:
        #print(data[counter][22,13]["y"])
        return getHypothenuses(data[counter])
    else:
        ani.event_source.stop()

def getHypothenuses(a):
     return np.sqrt(np.square(a['x'].astype(np.float)) + np.square(a['y'].astype(np.float))).clip(0, 255).astype(np.uint8)


# imshow(array)
im = plt.imshow(f(), animated=True)


def updatefig(*args):
    im.set_array(f())
    return im,

ani = animation.FuncAnimation(fig, updatefig, interval=100, blit=True)
plt.show()