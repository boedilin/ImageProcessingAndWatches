import numpy as np
import sys

if len(sys.argv) < 2:
    print("!____________________________add a file to read as parameter_________________!")
    print("!----------------------------------------------------------------------------!")

data = np.load(sys.argv[1])

#in einem for loop alle y-x-sad-werte von einem block ausgeben

for value in range(data.shape[0]):
    a=data[value][14,7]["sad"]
    b=data[value][15,7]["sad"]
    c=data[value][16,7]["sad"]
    d=data[value][17,7]["sad"]
    e=data[value][18,7]["sad"]
    f=data[value][19,7]["sad"]
    g=data[value][20,7]["sad"]
    h=data[value][21,7]["sad"]
    i=data[value][22,7]["sad"]
    j=data[value][23,7]["sad"]
    k=data[value][24,7]["sad"]
    print(a+b+c+d+e+f+g+h+j+i+k)