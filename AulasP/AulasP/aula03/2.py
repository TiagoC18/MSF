import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

t=np.linspace(0,4,1000)
g=9.8
vt=6.8
yt=(vt**2/g)*np.log(np.cosh(g*t/vt))
plt.plot(t, yt)
vinst=vt*np.tanh(g*t/vt)
ainst=g/np.cosh(g*t/vt)**2
plt.plot(t, vinst)
plt.plot(t, ainst)
plt.show()



t = sym.Symbol('tempo', real=True, positive=True)
vt = sym.Symbol('vt', real=True, positive=True)
g = sym.Symbol('g', real=True, positive=True)
vi = sym.diff((vt**2)/g * (sym.log(sym.cosh(g*t/vt))),t,1)
ay=sym.simplify(vi)
print('velocidade instantanea=', ay)

vi2 = sym.diff((vt**2)/g * (sym.log(sym.cosh(g*t/vt))),t,2)
ay2=sym.simplify(vi2)
print('aceleração instantanea=', ay2)

ayT= g-(g/vt**2)*vi*sym.Abs(vi)
