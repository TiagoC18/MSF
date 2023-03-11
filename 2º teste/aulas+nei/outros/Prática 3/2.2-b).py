import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

tempo = np.linspace(0, 4)

vT = sym.Symbol("vT")
g = sym.Symbol("g")
t = sym.Symbol("t")

d = sym.Derivative((vT**2)/g * sym.log(sym.cosh(g*t/vT)), t, evaluate=True)
d_simp = sym.simplify(d)

print("v(t) = ", d_simp)

plt.xlabel("Tempo (s)")
plt.ylabel("Velocidade (m/s)")
plt.plot(tempo, 6.80*np.tanh(9.8*tempo/6.80))

