#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 09:36:29 2017

@author: Linda
"""
import numpy as np
import matplotlib.pyplot as plt

directory = "14.12.17/run2_-13sec_greiner/"
timestamps = np.loadtxt(directory+"timestamps_of_minimas.txt")
y_deviation = []
x_time = []
x_time_rez = []

first_timestamp = timestamps[0]
reference_value = -14

for i in range(len(timestamps)):
    if i != 0 and timestamps[i] <= 300000000:
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

print(f(400))


time = np.arange(0.1, 10, 0.00001)
plt.plot(time, f(time), 'k')
plt.ylabel('Error of Measurement (sec)')
plt.xlabel('Duration of Measurement (sec)')
plt.show()
        

        

        


    
    
    
