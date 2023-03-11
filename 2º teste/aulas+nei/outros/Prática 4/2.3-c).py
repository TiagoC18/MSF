import numpy as np

t0 = 0
tf = 4
dt = 0.001
g = 9.8
n = int((tf-t0)/dt)

t = np.linspace(0, 4, n)
v = np.empty(n)
v[0] = 0

for i in range(n-1):
    v[i+1] = v[i] + dt*g

for i in range(n-1):
    if ((3-dt) < t[i] < (3+dt)):
        print("dt, t, v =", dt, t[i], v[i])