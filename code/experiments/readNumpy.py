import numpy as np

data = np.load('test.npy')
frame = data[0]
print('Captured %d frames' % data.shape[0])