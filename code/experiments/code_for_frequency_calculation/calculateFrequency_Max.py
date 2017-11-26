#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelmax
from scipy.signal import argrelmin

timestampsNotCleared = np.loadtxt("different_position_records/up/80min/timestamps.txt")
x = np.loadtxt("different_position_records/up/80min/xValues.txt")
y = np.loadtxt("different_position_records/up/80min/yValues.txt")
sad = np.loadtxt("different_position_records/up/80min/sadValues.txt")
movement_sum = np.empty(x.shape[0])
s = np.empty(x.shape[0])
timestamps = np.empty(x.shape[0])
counter = 0
index = 0
alpha = 0.01
frame_width = 10

for value in range(x.shape[0]):
    if x[value] != 0 and y[value]!= 0 and sad[value] != 0:
         movement_sum[index] = abs(x[value]) + abs(y[value])
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

movement_sum = np.trim_zeros(movement_sum, 'b')
s = np.trim_zeros(s, 'b')
timestamps = np.trim_zeros(timestamps, 'b')

mean_movement = np.mean(movement_sum)

movement_sum_min = argrelmax(movement_sum)[0]
smax = argrelmax(s)[0]
smin = argrelmin(s)[0]

firsttimestamp = 0
lasttimestamp = 0
plottimestamp = np.empty(smax.size)
smin_plot = np.empty(smax.size)
check_min = (s[smin[(smin.size - 50)]] + s[smin[(smin.size - 100)]] + s[smin[(smin.size - 10)]])/3
check_max = (s[smax[50]] +  s[smax[100]] +  s[smax[10]])/3
range_min_max = check_max - check_min

lower_limit_maxima = mean_movement + range_min_max*0.28
last_index = smax[0]

          
for max_index in smax:
    if s[max_index] > lower_limit_maxima and max_index - last_index > 3:
        counter += 1
        plottimestamp[counter] = timestamps[ max_index ]
        smin_plot[counter] = s[max_index]
        if firsttimestamp == 0:
            firsttimestamp = timestamps[ max_index ]
        lasttimestamp = timestamps[ max_index ] 
        last_index = max_index
    
print(check_min)
print(check_max)
print(range_min_max)
print(counter)
print("mean", mean_movement)
print(lasttimestamp)
smin.tofile("differents_time_records/10sec/2_record/smin.txt", sep="\n")

duration = ( lasttimestamp - firsttimestamp - 1 ) / 1000 / 1000
print(duration)

frequencyXY = 1 / (duration / counter * 2)
print(frequencyXY)

number_strokes = frequencyXY*7200

seconds_off_per_day = 24*3600 - (number_strokes*24*0.166666)
print("seconds off per day: ", seconds_off_per_day)


plt.plot(timestamps, s, 'b-', label='sum of x and y-factors of motion per frame')
#plt.plot(timestamps, y, 'r*', label='sum of y-factor of motion per frame')
plt.plot(plottimestamp, smin_plot, 'g*', label='xmax')
 
plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
