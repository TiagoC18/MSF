import numpy as np
import matplotlib.pyplot as plt


dt=0.1 # INPUT
tf=3.0
t0=0
n=np.int((tf-t0)/dt+0.1)
print('n = ',n)
t=np.zeros(n+1)
vy=np.zeros(n+1)
y=np.zeros(n+1)
g=9.80
v0y=0
y0=0
t[0]=t0
vy[0]=v0y
y[0]=y0

for i in range(n): # Método de Euler
    t[i+1]=t[i]+dt
    ax=g
    vy[i+1]=vy[i]+ax*dt
    y[i+1]=y[i]+vy[i]*dt

for i in range(n):
    if t[i+1] > 3-2*dt and t[i+1] < 3+2*dt:
        print('dt, t, vy= ',dt,t[i+1],vy[i+1])


#a
print("A acelaraçao é igual a derivada da velocidade a dividir pela derivada do tempo.")
#b

#c
print("Ao alterar se o passo a velocidade no instante 3 nao muda")
#d
print("v= ",g*3, "velociade exata que é igual ")

print("posiçao")

for i in range(n):
    if t[i+1] > 2-2*dt and t[i+1] < 2+2*dt:
        print('dt, t, y = ',dt,t[i+1],y[i+1])

print("passo: 0.01    y(2s)=19.50")
print("passo: 0.001    y(2s)=19.60")
print("yexato=",(1/2)*g*(2**2))

x=[0.1,0.01]#passo
y=[0.98,0.10] #desvio
plt.plot(x,y)
plt.xlabel("Passo")
plt.ylabel("Desvio")
plt.show()
print("desvio é proporcional ao passo")