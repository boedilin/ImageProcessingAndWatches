import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(100)
y = np.random.randn(100) + 5
print(x)
# normal distribution center at x=0 and y=5
plt.hist2d(x, y, bins=40)
plt.show()