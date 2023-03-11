import numpy as np
import matplotlib.pyplot as plt

m = 60 + 12
Cres = 0.9
A = 0.5
p = 1.225
u = 0.01
g = 9.8
P = 0.48 * 735.4975
vi = 0.5
t0 = 0
tf = 2000
dt = 0.001
tetai = np.radians(4)
tetaf = np.radians(1)

n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)

a = np.empty(n)
v = np.empty(n)
x = np.empty(n)

a[0] = 0
v[0] = vi
x[0] = 0

for i in range(n-1):
    v[i] = np.sqrt(v[i]*2)
    if (x[i] <= 1500):
        a[i] = -ug - (Cres/(2m))Ap(v[i])v[i] + \
            P/(mv[i]) - gnp.sin(tetai)
    else:
        a[i] = -ug - (Cres/(2m))Ap(v[i])v[i] + \
            P/(mv[i]) + gnp.sin(tetaf)
    v[i+1] = v[i] + a[i]dt
    x[i+1] = x[i] + v[i]*dt

    if x[i] < 2000 + dt and x[i+1] > 2000-dt:
        print("Tempo quando atinge 2km = ", t[i])
        break