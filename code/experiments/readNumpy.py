import numpy as np

data = np.load('my_video.npy')
thefile = open('my_video.txt', 'w')
list = data[401].tolist()

for item in list:
  thefile.write("%s\n" % item)


list = data[300].tolist()
print(data[300].shape)
for item in list:
    print("asd")
print('Captured %d frames' % data.shape[0])