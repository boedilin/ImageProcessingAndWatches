

import numpy as np
import matplotlib.pyplot as plt
timestamps = np.loadtxt("testSadtimestamps.txt")
xySad = np.load("myTest.npy")
ydata = np.empty(xySad.shape[0])
diff = np.empty(20)
freq = np.empty(20)
counter = 0

for value in range(xySad.shape[0]):
    sad = np.amax(xySad[value]["sad"])
    if sad >= 300:
        ydata[value] = 100
        print("True")
    else:
        ydata[value] = -100
        diff[counter] = timestamps[value]
        counter += 1
        print("False")  
for i in range(diff.size-2):
    freq[i] = diff[i+1]-diff[i]
    print(freq[i])
def funcSinus(x, a, b, c):
    return np.sin(x) + a + b + c

plt.plot(timestamps, ydata, 'b-', label='data')

plt.grid(b=True, which='both', color='0.65',linestyle='-')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()