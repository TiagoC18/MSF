import numpy as np
import matplotlib.pyplot as plt

m = 60 + 12
Cres = 0.9
A = 0.3
p = 1.225
u = 0.004
g = 9.8
P = 0.48 * 735.4975
vi = 0.5
t0 = 0
tf = 100
dt = 0.001
tolerancia = 0.00001

n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)

a = np.empty(n)
v = np.empty(n)
x = np.empty(n)

a[0] = 0
v[0] = vi
x[0] = 0

for i in range(n-1):
    v[i] = np.sqrt(v[i]**2)
    a[i] = -u*g - (Cres/(2*m))*A*p*(v[i])*v[i] + P/(m*v[i])
    v[i+1] = v[i] + a[i]*dt
    x[i+1] = x[i] + v[i]*dt

    v[n-1] = np.sqrt(v[n-1]**2)

    if (v[i]-v[i-1] < tolerancia):
        vt = v[i]
        print("Velociadade Terminal = ", vt)
        break
