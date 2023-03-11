import matplotlib.pyplot as plt
import numpy as np

v0 = 100/3.6
dt = 0.001
g = 9.8
t0 = 0
tf = 2
omega = -10
m = 0.45
r = 0.11
area = np.pi*r**2
den = 1.225
mag = 0.5*den*area*r
teta = np.radians(16)

vt = 100/3.6

n = int((tf-t0)/dt)
t = np.linspace(t0, tf, n)

vx = np.empty(n)
vy = np.empty(n)
vz = np.empty(n)

ax = np.empty(n)
ay = np.empty(n)
az = np.empty(n)

x = np.empty(n)
y = np.empty(n)
z = np.empty(n)

x[0] = 0
y[0] = 0
z[0] = 0

vx[0] = v0 * np.cos(teta)
vy[0] = v0 * np.sin(teta)
vz[0] = 0

d = g/vt**2

for i in range(n-1):
    t[i+1] = t[i] + dt
    vv = np.sqrt(vx[i]**2 + vy[i]**2 + vz[i]**2)
    amx = (-omega*vy[i]*mag)/m
    amy = (omega*vx[i]*mag)/m

    ax[i] = -d*vx[i]*abs(vv) + amx
    ay[i] = -d*abs(vv)*vy[i]-g + amy
    az[i] = -d*abs(vv)*vz[i]

    vy[i+1] = vy[i] + ay[i]*dt
    vx[i+1] = vx[i] + ax[i]*dt
    vz[i+1] = vz[i] + az[i]*dt

    y[i+1] = y[i] + vy[i] * dt
    x[i+1] = x[i] + vx[i] * dt
    z[i+1] = z[i] + vz[i] * dt


for i in range(n-1):
    if (x[i+1] > 20) and (0 < y[i+1] < 2.4) and (-3.75 < z[i+1] < 3.75):
        print("Golo")
        print("A altura da bola vai ser de ", y[i+1], " metros")
        break
