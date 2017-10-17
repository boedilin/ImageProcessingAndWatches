import numpy as np
import sys

if len(sys.argv) < 2:
    print("!____________________________add a file to read as parameter_________________!")
    print("!----------------------------------------------------------------------------!")

data = np.load(sys.argv[1])
myfile = open("testYAbsSum.txt", "a")

#in einem for loop alle y-x-sad-werte von einem block ausgeben

for value in range(data.shape[0]):
     myfile.write(str(np.abs(data[value]["y"]).sum())+"\n")
    #print(np.abs(data[value]["x"]).sum())