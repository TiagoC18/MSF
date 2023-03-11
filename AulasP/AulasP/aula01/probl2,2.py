import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

t=np.linspace(0,4,1000)
vt=6.8
g=9.8
y=((vt**2)/g)*(np.log(np.cosh(g*t/vt)))  #lei do movimento
plt.plot(t,y)

x2=vt*np.tanh((g*t)/vt)  # velociade instantanea derivada da lei do movimento
plt.plot(t,x2)

x3=g/(np.cosh((g*t)/vt)**2)   #acelaraçao instantanea derivada da velocidade isntantanea
plt.plot(t,x3)
plt.show()



t = sym.Symbol('t', real=True, positive=True)
v= sym.Symbol('v(t)', real=True, positive=True)
vt = sym.Symbol('vt', real=True, positive=True)
g = sym.Symbol('g', real=True, positive=True)

y2=sym.diff(((vt**2)/g)*(sym.log(sym.cosh(g*t/vt))),t,1)
vi=sym.simplify(y2)
print('velocidade instantanea=',vi)


y3=sym.diff(((vt**2)/g)*(sym.log(sym.cosh(g*t/vt))),t,2)
a=sym.simplify(y3)
print('acelaraçao=',a)


print(y3.equals(g - g / vt ** 2 * vi ** 2)) #Mostra que a acelaraçao da formula dada é igual a calculada anteriormente

grav=9.80
vt=6.80
altura=20.0
ext=altura*grav/vt**2
ex=np.exp(ext)
gt=np.arccosh(ex)
tempo=gt*vt/grav
print('gt/vt= ',gt,'    tempo chegada ao solo = ',tempo)
temlivre=np.sqrt(2*altura/grav)
print(' tempo queda livre ao solo = ',temlivre)
veloc=vt*np.tanh(grav*tempo/vt)
print(' velocidade(solo) = ',veloc)
acele=grav/np.cosh(grav*tempo/vt)**2
print(' acelera(solo) = ',acele)