import matplotlib.pyplot as plt
import numpy as np

dt=0.01
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

plt.scatter(t,x)
plt.show()