import numpy as np
import matplotlib.pyplot as plt

T = np.array([200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100])
E = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7])

x = T
y = E

plt.xlabel("T (K)")
plt.ylabel("E (J)")
plt.scatter(x,y)