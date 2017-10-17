import numpy as np
import sys

if len(sys.argv) < 2:
    print("!____________________________add a file to read as parameter_________________!")
    print("!----------------------------------------------------------------------------!")

data = np.load(sys.argv[1])
myfileX = open("testXAbsSum.txt", "a")
myfileY = open("testYAbsSum.txt", "a")
myfileSAD = open("testSADAbsSum.txt", "a")

#in einem for loop alle y-x-sad-werte von einem block ausgeben

for value in range(data.shape[0]):
     myfileX.write(str(np.abs(data[value]["x"]).sum())+"\n")
     myfileY.write(str(np.abs(data[value]["y"]).sum())+"\n")
     myfileSAD.write(str(np.abs(data[value]["sad"]).sum())+"\n")
    #print(np.abs(data[value]["x"]).sum())