import numpy as np

t0 = 0
tf = 4
dt = 0.01
vo = 0
g = 9.8
n = int((tf-t0)/dt)

t = np.linspace(0, 4, n)
v = np.empty(n)

for i in range(n-1):
    v[i+1] = v[i] + g*dt

for i in range(n-1):
    if ((3-dt) < t[i] < (3+dt)):
        print("dt, t, v =", dt, t[i], v[i])