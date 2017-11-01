#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelmin

timestamps = np.loadtxt("differents_time_records/10min/timestamps.txt")
xySad = np.load("differents_time_records/10min/myTest1.npy")
x = np.empty(xySad.shape[0])
y = np.empty(xySad.shape[0])
sad = np.empty(xySad.shape[0])
counter = 0
counterxy = 0
index = 0

#==============================================================================
# for value in range(xySad.shape[0]):
#     x[index] = np.sum(abs(xySad[value]["x"]))
#     y[index] = np.sum(abs(xySad[value]["y"]))
#     sad[index] = np.sum(xySad[value]["sad"])
#     index = index + 1;
#   
#==============================================================================
for value in range(xySad.shape[0]):
     x[index] = abs(xySad[value][0])
     y[index] = abs(xySad[value][1])
     sad[index] = xySad[value][2]
     index = index + 1;

xmin = argrelmin(x)[0]
ymin = argrelmin(y)[0]
sadmin = argrelmin(sad)[0]
firsttimestamp = 0
lasttimestamp = 0

for index in sadmin:
    if x[index] != 0 and y[index]!= 0 and sad[index] != 0:
        if sad[index] < 190000:
            counter += 1
            
for index in xmin:
    if x[index] != 0 and y[index]!= 0 and sad[index] != 0:
        if x[index] < 650 and y[index] < 650:
            counterxy += 1
            if firsttimestamp == 0:
                firsttimestamp = timestamps[ index ]
            lasttimestamp = timestamps[ index ]    
   
print(counter)
print(counterxy)

duration = ( lasttimestamp - firsttimestamp - 1 ) / 1000 / 1000
print(duration)

frequencySAD = 1 / (duration / counter * 2)
frequencyXY = 1 / (duration / counterxy * 2)
print(frequencySAD)
print(frequencyXY)

plt.plot(timestamps, x, 'b-', label='sum of x-factor of motion per frame')
plt.plot(timestamps, y, 'r-', label='sum of y-factor of motion per frame')

plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()