import numpy as np
import matplotlib.pyplot as plt

dt=0.0001
tf=1.0
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
v=np.empty(n+1)

#metodo de euler
g=9.80
v0=100*1000/3600 #m/s
ang=(10*np.pi)/180 #rad
vx[0]=v0*np.cos(ang)
vy[0]=v0*np.sin(ang)
vt=100*1000/3600
D=g/(vt**2)

#com resistencia do ar
for i in range(n):
    v[i]=(vy[i]**2+vx[i]**2)**0.5
    ay[i]=-g-D*vy[i]*v[i]
    vy[i+1]=vy[i]+ay[i]*dt
    y[i+1]=y[i]+vy[i]*dt
    ax[i]=-D*vx[i]*v[i]
    vx[i+1]=vx[i]+ax[i]*dt
    x[i+1]=x[i]+vx[i]*dt
    #altura maxima
    if (y[i-1]<y[i] and y[i+1]<y[i]):
        ymax=y[i+1]
    #alcance maximo
    if (y[i+1]*y[i]<0):
        xmax=x[i+1]
        
#sem resistencia do ar
vxx=np.empty(n+1)
vyy=np.empty(n+1)
axx=np.empty(n+1)
ayy=np.empty(n+1)
xx=np.empty(n+1)
yy=np.empty(n+1)
vxx[0]=v0*np.cos(ang)
vyy[0]=v0*np.sin(ang)
for i in range(n):
    ayy[i]=-g
    vyy[i+1]=vyy[i]+ayy[i]*dt
    yy[i+1]=yy[i]+vyy[i]*dt
    axx[i]=0
    vxx[i+1]=vxx[i]+axx[i]*dt
    xx[i+1]=xx[i]+vxx[i]*dt
    
fig, ax = plt.subplots(1)
ax.plot(x,y, label="Com resistencia do ar")
ax.plot(xx,yy, label="Sem resistencia do ar")
ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_title("Grafico da trajetoria")
plt.legend()
plt.grid()
plt.show()

print("Com resistencia do ar: ")
print("altura maxima= ", ymax)
print("alcance maximo= ", xmax)