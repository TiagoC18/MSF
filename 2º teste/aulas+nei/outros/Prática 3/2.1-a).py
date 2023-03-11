import numpy as np
import matplotlib.pyplot as plt

vA = 70000/3600
aP = 2.0

t = np.linspace(0, 25, 100)

plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.plot(t, vA*t, label="Carro A")
plt.plot(t, t**2, label="Carro Patrulha")
plt.legend()