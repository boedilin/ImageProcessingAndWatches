#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelmin

timestampsNotCleared = np.loadtxt("differents_time_records/20min/timestamps_black_white.txt")
xySad = np.load("differents_time_records/20min/motion_vectors_black_white.npy")
x = np.empty(xySad.shape[0])
y = np.empty(xySad.shape[0])
timestamps = np.empty(xySad.shape[0])
counter = 0
index = 0

for value in range(xySad.shape[0]):
    if xySad[value][0] != 0 and xySad[value][1]!= 0 and xySad[value][2] != 0:
         x[index] = abs(xySad[value][0])
         y[index] = abs(xySad[value][1])
         timestamps[index] = timestampsNotCleared[value]
         index = index + 1;

x = np.trim_zeros(x)
y = np.trim_zeros(y)
timestamps = np.trim_zeros(timestamps)
xmin = argrelmin(x)[0]
ymin = argrelmin(y)[0]

firsttimestamp = 0
lasttimestamp = 0

          
for min_index in xmin:
    y_check = 0
    check_min_in_ymin = False
    if np.argwhere(ymin == min_index).size != 0:
        check_min_in_ymin = True
        y_check = y[min_index]
    elif np.argwhere(ymin == (min_index + 1)).size != 0:
        check_min_in_ymin = True
        y_check = y[min_index+1]
    elif np.argwhere(ymin == (min_index -1)).size != 0:
        check_min_in_ymin = True
        y_check = y[min_index-1]
    if x[min_index] < 1700 and check_min_in_ymin and y_check < 1700:
        counter += 1
        if firsttimestamp == 0:
            firsttimestamp = timestamps[ min_index ]
        lasttimestamp = timestamps[ min_index ] 
   
print(counter)

duration = ( lasttimestamp - firsttimestamp - 1 ) / 1000 / 1000
print(duration)

frequencyXY = 1 / (duration / counter * 2)
print(frequencyXY)


plt.plot(timestamps, x, 'b-', label='sum of x-factor of motion per frame')
plt.plot(timestamps, y, 'r-', label='sum of y-factor of motion per frame')

plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()