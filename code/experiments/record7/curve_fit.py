import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

xySad = np.load("myTest.npy")
ydata = np.empty(xySad.shape[0])
xdata = np.empty(xySad.shape[0])
counter = 0

for value in range(xySad.shape[0]):
    xSum = np.abs(xySad[value]["x"]).sum()
    ydata[value] = xSum
    counter += 1
    xdata[value] = counter
def funcSinus(x, a, b, c):
    return np.sin(x) + a + b + c
"""
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, 'b-', label='data')

popt, pcov = curve_fit(func, xdata, ydata)
plt.plot(xdata, func(xdata, *popt), 'r-', label='fit')

popt, pcov = curve_fit(func, xdata, ydata, bounds=(0, [3., 2., 1.]))
plt.plot(xdata, func(xdata, *popt), 'g--', label='fit-with-bounds')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
"""
plt.plot(xdata, ydata, 'b-', label='data')

popt, pcov = curve_fit(funcSinus, xdata, ydata)
plt.plot(xdata, funcSinus(xdata, *popt), 'r-', label='fit')

popt, pcov = curve_fit(funcSinus, xdata, ydata, bounds=(0, [3., 2., 1.]))
plt.plot(xdata, funcSinus(xdata, *popt), 'g--', label='fit-with-bounds')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()