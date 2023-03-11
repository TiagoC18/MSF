import numpy as np
import matplotlib.pyplot as plt

dx=0.0001
xf=2.0
x0=-2.0
n=int((xf-x0)/dx)

x=np.linspace(x0, xf, n+1)
Ep=np.empty(n+1)

#metodo de euler
g=9.80
m=1.5
k=1.2
alpha=-0.01
 
Ep0=999
#x2=0

#com resistencia do ar
for i in range(n):
    Ep=0.5*k*x**2+alpha*x**3
    if(x[i]==0):
        Ep0=Ep[i]
 #   if(Ep[i]>=2 and Ep[i]<2.01):
  #      x2=x[i]
    
    
fig, ax = plt.subplots(1)
ax.plot(x,Ep)
ax.set_xlabel("x (m)")
ax.set_ylabel("Energia potencial (J)")
ax.set_title("Diagrama Energia Potencial")
plt.grid()
plt.show()

print("Exercicio 2, alinea a)")
print(Ep0)
#print(x2)