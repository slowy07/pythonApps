import matplotlib.pyplot as plt

import numpy as np

# x co-ordinates
x = np.arange(0, 9)
A = np.array([x, np.ones(9)])

# linearly generated sequence
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24]
# obtaining the parameters of regression line
w = np.linalg.lstsq(A.T, y)[0]

line = w[0] * x + w[1]  # regression line
plt.plot(x, line, "r-")
plt.plot(x, y, "o")
plt.show()
