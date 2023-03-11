import numpy as np
import matplotlib.pyplot as plt

T = np.arange(0, 10, 1)
D = np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329])

x = T
y = D

plt.xlabel("tempo (min)")
plt.ylabel("distância (km)")
plt.scatter(x, y)