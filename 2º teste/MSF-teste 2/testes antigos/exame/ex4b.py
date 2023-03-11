import numpy as np
import matplotlib.pyplot as plt

dt=0.0001
tf=8.0
t0=0
n=int((tf-t0)/dt)

t=np.linspace(t0, tf, n+1)
vx=np.empty(n+1)
vy=np.empty(n+1)
ax=np.empty(n+1)
ay=np.empty(n+1)
x=np.empty(n+1)
y=np.empty(n+1)
v=np.empty(n+1)

#Fx=-k*x-3*a*x**2
#metodo de euler
k=1.2  #N/m
a=-0.01  #N/m**2
g=9.80
v0=2.0 #m/s
vx[0]=v0
vy[0]=0
x[0]=3.5

#
for i in range(n):
    v[i]=(vy[i]**2+vx[i]**2)**0.5
    ay[i]=-g
    vy[i+1]=vy[i]+ay[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    ax[i]=-k*x[i]-3*a*x[i]**2
    vx[i+1]=vx[i]+ax[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    
fig, ax = plt.subplots(1)
ax.plot(t,x)
ax.set_xlabel("t (s)")
ax.set_ylabel("x (m)")
ax.set_title("Grafico da trajetoria")
plt.grid()
plt.show()