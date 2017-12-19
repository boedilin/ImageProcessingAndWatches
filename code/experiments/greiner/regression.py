#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:36:29 2017

@author: Linda
"""
import numpy as np
import matplotlib.pyplot as plt

directory = "14.12.17/run3_-5sec_greiner/"
timestamps = np.loadtxt(directory+"timestamps_of_minimas.txt")
y_deviation = []
x_time = []
x_time_rez = []

first_timestamp = timestamps[0]
reference_value = -5

for i in range(len(timestamps)):
    if i != 0:
        x_time.append(timestamps[i] - first_timestamp)
        x_time_rez.append(1/((timestamps[i] - first_timestamp)/1000000))
        duration = (timestamps[i] - first_timestamp) / i;
        y_deviation.append(abs(reference_value - (3600-(duration/1000000*18000))*24))
        
    
A = np.matrix([x_time_rez, [1]*len(x_time_rez)]).transpose()

A_transpose = A.transpose()

A_transpose_with_y = np.dot(A_transpose,y_deviation)

A_trans_y = []
A_trans_y.append(A_transpose_with_y.item((0, 0)))
A_trans_y.append(A_transpose_with_y.item((0, 1)))


a_b = np.linalg.tensorsolve(np.dot(A_transpose,A), A_trans_y)

print( a_b)

a = a_b.item((0, 0))
b = a_b.item((0, 1))

def f(x):
    return a/x + b

print(f(00))


time = np.arange(50, 600, 1)
xtime_new = []
ydeviation_new = []
for i in range(len(timestamps)):
    if timestamps[i]/1000000 <= 600 and i % 50 == 0 :
        xtime_new.append(x_time[i]/1000000)
        ydeviation_new.append(y_deviation[i])
plt.subplot(211)
plt.plot(xtime_new,ydeviation_new, 'r*')
plt.ylabel('Error of Measurement (s)')
plt.xlabel('Duration of Measurement (s)')

plt.subplot(212)
plt.plot( time, f(time), 'k')
plt.ylabel('Error of Measurement (s)')
plt.xlabel('Duration of Measurement (s)')
plt.show()
        

        

        


    
    
    
