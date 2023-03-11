import numpy as np

t0 = 0
tf = 4
dt = 0.01
g = 9.8
n = int((tf-t0)/dt)

t = np.linspace(0, 3, n)
v = np.empty(n)
v[0] = 0
x = np.empty(n)
x[0] = 0

for i in range(n-1):
    v[i+1] = v[i] + g*dt
    x[i+1] = x[i] + v[i]*dt

for i in range(n-1):
    if ((2-dt) < t[i] < (2+dt)):
        print("dt, t, x =", dt, t[i], x[i])