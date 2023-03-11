import numpy as np
import matplotlib.pyplot as plt

vi = 100/3.6
teta = np.radians(16)
t0 = 0
tf = 1.5
dt = 0.001
g = 9.8
n = int(tf/dt)
t = np.linspace(t0, tf, n)
vt = 100/3.6

y = np.empty(n)
y[0] = 0

x = np.empty(n)
x[0] = 0

vx = np.empty(n)
vx[0] = vi * np.cos(teta)

vy = np.empty(n)
vy[0] = vi * np.sin(teta)

ax = np.empty(n)
ax[0] = 0

ay = np.empty(n)
ay[0] = -g

v = np.empty(n)
v[0] = vi

d = g/vt**2

for i in range(n-1):
    t[i+1] = t[i] + dt
    v[i] = np.sqrt(vx[i]**2+vy[i]**2)

    ax[i] = -d*abs(v[i])*vx[i]
    ay[i] = -g - d*abs(v[i])*vy[i]

    vx[i+1] = vx[i] + ax[i]*dt
    vy[i+1] = vy[i] + ay[i]*dt

    x[i+1] = x[i] + vx[i+1]*dt
    y[i+1] = y[i] + vy[i+1]*dt


for i in range(n-1):
    if (x[i+1] > 20) and (0 < y[i+1] < 2.4):
        print("Golo!")
        print("A altura da bola vai ser de ", y[i+1], " metros")
        break
