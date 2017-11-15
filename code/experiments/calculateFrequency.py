#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelmax

timestampsNotCleared = np.loadtxt("differents_time_records/48min/timestamps_black_white.txt")
xySad = np.load("differents_time_records/48min/motion_vectors_black_white.npy")
movement_sum = np.empty(xySad.shape[0])
s = np.empty(xySad.shape[0])
timestamps = np.empty(xySad.shape[0])
counter = 0
index = 0
alpha = 0.01
frame_width = 10

for value in range(xySad.shape[0]):
    if xySad[value][0] != 0 and xySad[value][1]!= 0 and xySad[value][2] != 0:
         movement_sum[index] = abs(xySad[value][0]) + abs(xySad[value][1])
         if index < frame_width:
             s[index] = movement_sum[index]
         else:
             s[index] = alpha * movement_sum[index] + (1 - alpha ) * s[index - 1 ]
             s[index] = 0
             for i in range(0,frame_width):
                 s[index] = s[index] + movement_sum[ index - i ]
             s[index] =  s[index] / frame_width
         timestamps[index] = timestampsNotCleared[value]
         index = index + 1;

movement_sum = np.trim_zeros(movement_sum)
s = np.trim_zeros(s)
timestamps = np.trim_zeros(timestamps)

mean_movement = np.mean(movement_sum)

movement_sum_min = argrelmax(movement_sum)[0]
smin = argrelmax(s)[0]

firsttimestamp = 0
lasttimestamp = 0
plottimestamp = np.empty(smin.size)
smin_plot = np.empty(smin.size)
upper_limit_minima = mean_movement + 295
last_index = smin[0]

          
for min_index in smin:
    if s[min_index] > upper_limit_minima and min_index - last_index > 3:
        counter += 1
        plottimestamp[counter] = timestamps[ min_index ]
        smin_plot[counter] = s[min_index]
        if firsttimestamp == 0:
            firsttimestamp = timestamps[ min_index ]
        lasttimestamp = timestamps[ min_index ] 
        last_index = min_index
   
print(counter)
print("mean", mean_movement)
print(lasttimestamp)
smin.tofile("differents_time_records/10sec/2_record/smin.txt", sep="\n")

duration = ( lasttimestamp - firsttimestamp - 1 ) / 1000 / 1000
print(duration)

frequencyXY = 1 / (duration / counter * 2)
print(frequencyXY)


plt.plot(timestamps, s, 'b-', label='sum of x-factor of motion per frame')
#plt.plot(timestamps, y, 'r*', label='sum of y-factor of motion per frame')
plt.plot(plottimestamp, smin_plot, 'g*', label='sum of xmin-factor of motion per frame')
 
plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
