import numpy as np

xValues = np.loadtxt("xValues.txt")
yValues = np.loadtxt("yValues.txt")
xPlusyValues_file = open("xPlusyValues.txt", "a")

for index in range (len(xValues)):
    xPlusyValues_file.write(str(xValues[index]+yValues[index])+"\n")
xPlusyValues_file.close()