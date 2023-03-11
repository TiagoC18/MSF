import numpy as np
import matplotlib.pyplot as plt

dx=0.0001
xf=5.0
x0=-5.0
n=int((xf-x0)/dx)

x=np.linspace(x0, xf, n+1)
Ep=np.empty(n+1)

#metodo de euler
g=9.80
m=1.5
k=1.2
alpha=-0.01
 

#com resistencia do ar
for i in range(n):
    Ep=0.5*k*x**2+alpha*x**3
    
fig, ax = plt.subplots(1)
ax.plot(x,Ep)
ax.set_xlabel("x (m)")
ax.set_ylabel("Energia potencial (J)")
ax.set_title("Diagrama Energia Potencial")
plt.grid()
plt.show()

print("Exercicio 4, alinea a)")