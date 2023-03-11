import numpy as np
import matplotlib.pyplot as plt

dt=0.0001
tf=1.0
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

#metodo de euler
g=9.80
m=0.057  #kg
v0=100*1000/3600 #m/s
ang=(10*np.pi)/180 #rad
vx[0]=v0*np.cos(ang)
vy[0]=v0*np.sin(ang)
vt=100*1000/3600
y[0]=0
x[0]=0
D=g/(vt**2)

Emec=0

#com resistencia do ar
for i in range(n):
    v[i]=(vy[i]**2+vx[i]**2)**0.5
    ay[i]=-g-D*vy[i]*v[i]
    vy[i+1]=vy[i]+ay[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    ax[i]=-D*vx[i]*v[i]
    vx[i+1]=vx[i]+ax[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    if (t[i]==0.8):
        Emec=0.5*m*v[i]**2+m*g*y[i]
    
fig, ax = plt.subplots(1)
ax.plot(x,y)
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Grafico da trajetoria")
plt.grid()
plt.show()

print("Energia Mecanica em t0.8 = ", Emec, "J")