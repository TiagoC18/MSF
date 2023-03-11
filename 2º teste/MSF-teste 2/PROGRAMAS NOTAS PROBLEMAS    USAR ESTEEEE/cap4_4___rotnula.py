import numpy as np
import matplotlib.pyplot as plt


dt=0.01
tf=2.0
t0=0
n=int((tf-t0)/dt)

t=np.linspace(t0, tf, n+1)
vx=np.empty(n+1)
vy=np.empty(n+1)
vz=np.empty(n+1)
ax=np.empty(n+1)
ay=np.empty(n+1)
az=np.empty(n+1)
y=np.empty(n+1)
x=np.empty(n+1)
z=np.empty(n+1)
v=np.empty(n+1)

#metodo de euler
g=9.80
v0=130*1000/3600 #m/s
ang=(10*np.pi)/180 #rad
vx[0]=v0*np.cos(ang)
vy[0]=v0*np.sin(ang)
vz[0]=0
x[0]=-10
y[0]=1
z[0]=0


vt=100*1000/3600
D=g/(vt**2)

for i in range(n):
    
    v[i]=((vx[i]**2)+(vy[i]**2)+(vz[i]**2))**0.5
        
    az[i]=0
    ay[i]=-D*v[i]*vy[i]-g
    ax[i]=-D*v[i]*vx[i]
    
    vz[i+1]=vz[i]+az[i]*dt
    vy[i+1]=vy[i]+ay[i]*dt
    vx[i+1]=vx[i]+ax[i]*dt
    
    z[i+1]=z[i]+vz[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    
    if (y[i-1]<y[i] and y[i+1]<y[i]):
        ymax=y[i+1]
    if (y[i+1]*y[i]<0):
        xmax=x[i+1]
    
    
#grafico
fig, ax = plt.subplots(1)
ax.plot(x,y)
ax.set_xlabel("posição x")
ax.set_ylabel("posição y")
ax.set_title("Grafico da Trajetoria")
plt.grid()
plt.show()

#respostas:
print(" alcance= ", xmax , "\n altura máx= ", ymax)