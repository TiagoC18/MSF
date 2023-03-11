import numpy as np
import matplotlib.pyplot as plt

T = np.array([200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100])
E = np.array([0.6950, 4.363, 15.53, 38.74, 75.08, 125.2, 257.9, 344.1, 557.4, 690.7])

x = T
y = E

plt.plot(np.log(x), np.log(y), "o")
a = np.polyfit(np.log(x), np.log(y), 1)

t = np.linspace(np.log(x[0])*0.9, np.log(x[-1])*1.1, 100)
plt.plot(x, a[0]*x+a[1])