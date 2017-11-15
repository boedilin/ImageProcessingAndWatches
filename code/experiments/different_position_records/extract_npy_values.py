import numpy as np

directory="up/80min"
data=np.load(directory+"/motion_vectors_80min_black_white.npy")
with open(directory+"/timestamps_40min_black_white.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
xValues = open(directory+"/xValues.txt", "a")
yValues = open(directory+"/yValues.txt", "a")
sadValues = open(directory+"/sadValues.txt", "a")
timestamps = open(directory+"/timestamps.txt", "a")

for index in range(len(array)):
    if ("None" not in array[index]) & (data[index][0] != 0) :
        xValues.write(str(data[index][0])+"\n")
        yValues.write(str(data[index][1])+"\n")
        sadValues.write(str(data[index][2])+"\n")
        timestamps.write(str(array[index]))

xValues.close()
yValues.close()
sadValues.close()