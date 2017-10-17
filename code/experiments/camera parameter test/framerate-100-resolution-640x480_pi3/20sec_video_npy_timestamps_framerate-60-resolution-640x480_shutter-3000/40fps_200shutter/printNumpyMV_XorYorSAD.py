import numpy as np
import sys

if len(sys.argv) < 2:
    print("!____________________________add a file to read as parameter_________________!")
    print("!----------------------------------------------------------------------------!")

data = np.load(sys.argv[1])
myfile = open("test2SAD.txt", "a")

#in einem for loop alle y-x-sad-werte von einem block ausgeben

for value in range(data.shape[0]):
    #a = np.sqrt(np.square(data[value]['x'].astype(np.float)) +np.square(data[value]['y'].astype(np.float)).astype(np.uint8))
    #myfile.write(str(a.sum())+"\n")
    myfile.write(str(np.abs(data[value]["sad"]).sum())+"\n")
    #print(np.abs(data[value]["x"]).sum())
    #print(a)