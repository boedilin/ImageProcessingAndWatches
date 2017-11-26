import numpy as np

directory="down/4hours"
data=np.load(directory+"/motion_vectors_4hours_black_white.npy")
with open(directory+"/timestamps_4hours_black_white.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
xValues = open(directory+"/xValues_plus_iframe.txt", "a")
yValues = open(directory+"/yValues_plus_iframe.txt", "a")
sadValues = open(directory+"/sadValues_plus_iframe.txt", "a")
timestamps = open(directory+"/timestamps_plus_iframe.txt", "a")

for index in range(len(array)):
    if ("None" in array[index]):
        xValues.write("10000"+"\n")
        yValues.write("10000"+"\n")
        sadValues.write("100000"+"\n")
        timestamps.write("0"+"\n")
    else:
        xValues.write(str(data[index][0])+"\n")
        yValues.write(str(data[index][1])+"\n")
        sadValues.write(str(data[index][2])+"\n")
        timestamps.write(str(array[index]))

xValues.close()
yValues.close()
sadValues.close()
timestamps.close()