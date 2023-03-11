import matplotlib.pyplot as plt
import numpy as np

dt=0.1
tf= 4.0
t0=0
x0=0
v0x=0

g=9.80

n= np.int((tf-t0)/dt+0.1)
print('n',n)

t=np.zeros(n+1)
x=np.zeros(n+1)
vx=np.zeros(n+1)

vx[0]=v0x
t[0]=t0
x[0]=x0
for i in range(n):
    t[i+1]=t[i]+dt
    vx[i]=g*t[i]
    x[i+1]=x[i]+vx[i]*dt

for i in range(n):
    if t[i+1] > 3-2*dt and t[i+1] < 3+2*dt:
         print('dt, t, vx= ',dt,t[i+1],vx[i+1])

print("Velocidades:")
print("v= ", g*3)
print(vx[3])

print("Posições:")
for i in range(n):
    if t[i+1] > 2-2*dt and t[i+1] < 2+2*dt:
         print('dt, t, x= ',dt,t[i+1],x[i+1])

print("Y exato= ", 0.5*g*4)

x=[0.1, 0.01]
y=[19.6-18.62, 19.6-19.502]
plt.plot(x,y)
plt.show()
