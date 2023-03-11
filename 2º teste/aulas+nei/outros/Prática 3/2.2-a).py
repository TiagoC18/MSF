import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4)

vT = 6.80
g = 9.8

plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.plot(t, (vT**2)/g * np.log(np.cosh(g*t/vT)))

