#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 13:57:12 2017

@author: Linda

=================
Direction field of motion vector
=================
"""
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.pyplot as plt

data = np.load('my_video.npy')

fig = plt.figure(num=1)
ax=fig.add_subplot(111)

#Normalize arrows
ax.quiver(data[50]["x"] ,data[50]["y"],data[51]["x"], data[51]["y"])

plt.xlabel(r"$x$")
plt.ylabel(r"$y$")
plt.show()
