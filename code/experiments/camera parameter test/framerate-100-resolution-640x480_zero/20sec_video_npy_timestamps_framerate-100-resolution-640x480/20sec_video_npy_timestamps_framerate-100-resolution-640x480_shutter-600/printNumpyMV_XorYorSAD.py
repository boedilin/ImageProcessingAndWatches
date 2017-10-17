import numpy as np
import sys

if len(sys.argv) < 2:
    print("!____________________________add a file to read as parameter_________________!")
    print("!----------------------------------------------------------------------------!")

data = np.load(sys.argv[1])

#in einem for loop alle y-x-sad-werte von einem block ausgeben

for value in range(data.shape[0]):
    print(data[value][9,7]["y"],";",data[value][9,8]["y"],";",data[value][9,9]["y"],";",data[value][9,10]["y"],";",data[value][9,11]["y"],";",data[value][9,12]["y"],";")