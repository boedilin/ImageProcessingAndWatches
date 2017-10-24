#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
timestamps = np.loadtxt("testSadtimestamps.txt")
xySad = np.load("myTest.npy")
x = np.empty(xySad.shape[0])
y = np.empty(xySad.shape[0])
counterx = 0
countery = 0
index = 0

for value in range(xySad.shape[0]):
    x[index] = np.sum(xySad[value]["x"])
    y[index] = np.sum(xySad[value]["y"])
    index = index + 1;
    
xbefore = x[0]
ybefore = x[0]
diffx = np.empty(x.shape[0])
diffy = np.empty(y.shape[0])

for i in range(x.shape[0]):
    if xbefore <= x[i] and i != 0:
        diffx[counterx] = timestamps[i-1]
        counterx = counterx + 1
    if ybefore <= y[i] and i != 0:
        diffy[countery] = timestamps[i-1]  
        countery = countery + 1
    xbefore = x[i]
    ybefore = y[i]
    
halfperiodx = np.empty(diffx.shape[0])
halfperiody = np.empty(diffy.shape[0])
periodxaverage = 0
periodyaverage = 0
countperiodx = 0
countperiody = 0
    
for i in range(diffx.shape[0]-2):
    halfperiodx[i] = diffx[i+1]-diffx[i]
    halfperiody[i] = diffy[i+1]-diffy[i]

periodx = np.empty(halfperiody.shape[0]//2)
periody = np.empty(halfperiody.shape[0]//2)
    
for i in range(periodx.shape[0]-1):
    if halfperiodx[i] >= 0 and halfperiodx[i+1] >= 0:
        periodx[i] = halfperiodx[i]+halfperiodx[i+1]
        periodxaverage = periodxaverage + periodx[i]
        countperiodx = countperiodx + 1
    if halfperiody[i] >= 0 and halfperiody[i+1] >=0:
        periody[i] = halfperiody[i]+halfperiody[i+1]
        periodyaverage = periodyaverage + periody[i]
        countperiody = countperiody + 1

periodxaverage = periodxaverage / countperiodx
periodyaverage = periodyaverage / countperiody
frequencyx = 1 / periodxaverage
frequencyy = 1 / periodyaverage
print(frequencyx)
print(frequencyy)

plt.plot(timestamps, x, 'b-', label='sum of x-factor of motion per frame')
plt.plot(timestamps, y, 'r-', label='sum of y-factor of motion per frame')

plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()