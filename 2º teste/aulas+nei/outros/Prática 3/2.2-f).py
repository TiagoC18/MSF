import numpy as np
import sympy as sym

vT = sym.Symbol("vT")
g = sym.Symbol("g")
t = sym.Symbol("t")

d = sym.Derivative((vT**2)/g * sym.log(sym.cosh(g*t/vT)), t, evaluate=True)
d_simp = sym.simplify(d)

d2 = sym.Derivative(d_simp, t, evaluate=True)
d2_simp = sym.simplify(d2)

print("v(t) = ", d_simp)
print("a(t) = ", d2_simp)

y0 = 20
g1 = 9.8
vT1 = 6.80

t1 = np.arccosh(10**(y0*g1/vT1**2))*vT1/g1
v = vT1*np.tanh(g1*t1/vT1)
a = g1/np.cosh(g1*t1/vT1)**2

print("Velocidade:", v, "m/s.")
print("Aceleração:", a, "m/s^2.")
