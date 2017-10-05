import numpy as np

data = np.load('test.npy')
dataX = np.empty((data.shape[0] * data.shape[1] * data.shape[2]), dtype=int ).reshape(data.shape[0] , data.shape[1] , data.shape[2])
dataY = np.empty(data.shape[0] * data.shape[1] * data.shape[2], dtype=int).reshape(data.shape[0] , data.shape[1] , data.shape[2])
dataSAD = np.empty(data.shape[0] * data.shape[1] * data.shape[2], dtype=int).reshape(data.shape[0] , data.shape[1] , data.shape[2])

for f in range(data.shape[0]):
    dataX[f] = data[f]["x"]
    dataY[f] = data[f]["y"]
    dataSAD[f] = data[f]["sad"]

np.save("testX.npy", dataX)
np.save("testY.npy", dataY)
np.save("testSAD.npy", dataSAD)