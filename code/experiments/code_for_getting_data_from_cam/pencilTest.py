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
data = np.load('testVertikal.npy')

counter = 0

print('Captured %d frames' % data.shape[0])
print(data[0]["sad"])

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

ani = animation.FuncAnimation(fig, updatefig, interval=200, blit=True)
plt.show()