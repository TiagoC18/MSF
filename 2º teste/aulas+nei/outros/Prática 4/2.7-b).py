import numpy as np

dt = 0.0001
tf = 4
t0 = 0
g = -9.80
n = int((tf-t0)/dt)

v = np.empty(n)
v[0] = 10
y = np.empty(n)
y[0] = 0
t = np.empty(n)
t[0] = 0

for i in range(n-1):
    t[i+1] = t[i]+dt
    v[i+1] = v[i] + g*dt
    y[i+1] = y[i] + v[i]*dt
    
for i in range(n):
    if (v[i] > (0-dt) and v[i] < (0+dt)):
        print("Altura máxima:", y[i], t[i] )