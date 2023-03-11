import sys
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

dt=0.001
tf=30
n=np.int(tf/dt+0.1)
print('n',n)
g = 9.80
L = 1

t=np.zeros(n+1)
x=np.zeros(n+1)
vp=np.zeros(n+1)
theta=np.zeros(n+1)
theta[0] = np.radians(1)
vp[0] = 0
tempos=[]

for i in range(n):
    t[i+1]=t[i] + dt
    ap = -g/L * np.sin(theta[i])
    vp[i+1] = vp[i] + ap*dt
    theta[i+1] = theta[i] + vp[i+1]*dt
    if i>1 and theta[i-1]<theta[i] and theta[i]>theta[i+1]:
        tempos.append(t[i])

for i in range(len(tempos)-1):
    periodo = abs(tempos[i] - tempos[i+1])
    print(periodo)

plt.plot(t,theta)
plt.show()