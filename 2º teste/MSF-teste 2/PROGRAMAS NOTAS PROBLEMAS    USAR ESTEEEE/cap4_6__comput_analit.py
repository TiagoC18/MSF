import numpy as np
import matplotlib.pyplot as plt

dt=0.01
tf=18.0
t0=0
n=int((tf-t0)/dt)

ymax=0
xmax=0

t=np.linspace(t0, tf, n+1)
vx=np.empty(n+1)
vy=np.empty(n+1)
ax=np.empty(n+1)
ay=np.empty(n+1)
x=np.empty(n+1)
y=np.empty(n+1)

#metodo de euler
A=1
o=0

m=1
k=1
w=(k/m)**0.5
g=9.80
v0=0 #m/s
vx[0]=v0
vy[0]=v0
x[0]=4
for i in range(n):
    ay[i]=0
    vy[i+1]=vy[i]+ay[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    ax[i]=-k*(A*np.cos(w*t[i]+o))
    vx[i+1]=vx[i]+ax[i]*dt
    x[i+1]=x[i]+vx[i]*dt

#analitico
vxx=-A*w*np.sin(w*t+o)

    
fig, ax = plt.subplots(1)
ax.plot(t,vx, label="computacional")
ax.plot(t,vxx, label="analitico")
ax.set_xlabel("t (s)")
ax.set_ylabel("vx (m/s)")
ax.set_title("Grafico da Velocidade")
plt.legend()
plt.grid()
plt.show()