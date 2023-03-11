import numpy as np
import matplotlib.pyplot as plt

dt=0.0001
tf=0.5
t0=0
n=int((tf-t0)/dt)

t=np.linspace(t0, tf, n+1)
vx=np.empty(n+1)
vy=np.empty(n+1)
vz=np.empty(n+1)
ax=np.empty(n+1)
ay=np.empty(n+1)
az=np.empty(n+1)
x=np.empty(n+1)
y=np.empty(n+1)
z=np.empty(n+1)
v=np.empty(n+1)

#metodo de euler
g=9.80
m=0.45  #kg
dAr=1.225 #kg/m**3
r=0.11 #m
Area=np.pi*r**2
wx=0 #rad/s
wy=400 #rad/s
wz=0 #rad/s
vx[0]=25 #m/s
vy[0]=5 #m/s
vz[0]=-50 #m/s
x[0]=0  #m
y[0]=0  #m
z[0]=23.8  #m
vt=100*1000/3600
D=g/(vt**2)

golo="nao foi golo"

for i in range(n):
    v[i]=(vy[i]**2+vx[i]**2)**0.5
    az[i]=-g-D*vz[i]*v[i]-0.5*Area*dAr*r*wz*vz[i]
    vz[i+1]=vz[i]+az[i]*dt
    z[i+1]=z[i]+vz[i]*dt
    ay[i]=-g-D*vy[i]*v[i]-0.5*Area*dAr*r*wy*vy[i]
    vy[i+1]=vy[i]+ay[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    ax[i]=-D*vx[i]*v[i]-0.5*Area*dAr*r*wx*vx[i]
    vx[i+1]=vx[i]+ax[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    if(x[i+1]>0 and y[i+1]>0 and y[i+1]<2.4 and z[i+1]>0 and z[i+1]<7.3):
        golo="foi golo"
        
        
fig, ax = plt.subplots(1)
ax.plot(t,x, label="x(t)")
ax.plot(t,y, label="y(t)")
ax.plot(t,z, label="z(t)")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Grafico da trajetoria")
plt.legend()
plt.grid()
plt.show()

print(golo)