import numpy as np
import matplotlib.pyplot as plt

P=0.4*735.4975
m=75
yalc=0.004
A=0.3
g=9.8
Cres=0.9
ro=1.225

###

dt=0.001
tf=100.0
t0=0
n=int((tf-t0)/dt)

t=np.linspace(t0, tf, n+1)
vx=np.empty(n+1)
ax=np.empty(n+1)
x=np.empty(n+1)
v=np.empty(n+1)

#metodo de euler
g=9.80
v0=1 #m/s
ang=(0*np.pi)/180 #rad
vx[0]=v0*np.cos(ang)
x0=0

x[0]=x0

vt=0
#D=g/(vt**2)

for i in range(n):
    
    v[i]=((vx[i])**2)**0.5
    ax[i]=-yalc*g-(Cres/(2*m))*A*ro*(v[i]*vx[i])+P/(m*vx[i])
    
    vx[i+1]=vx[i]+ax[i]*dt
    
    x[i+1]=x[i]+vx[i]*dt
    
    if(vx[i+1]-vx[i]<0.000001):
        vt=vx[i]

    
print("velocidade terminal = ", vt)    
y=0

#grafico
fig, ax = plt.subplots(1)
ax.plot(t,v, label="velocidade x")
ax.set_xlabel("tempo")
ax.set_ylabel("velocidade x")
ax.set_title("Grafico da Velocidade")
plt.legend()
plt.grid()
plt.show()