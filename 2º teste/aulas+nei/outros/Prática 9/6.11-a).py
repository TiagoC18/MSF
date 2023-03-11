import numpy as np
import matplotlib.pyplot as plt

v = 30/3.6
m = 75
Cres = 0.9
A = 0.3
p = 1.225
u = 0.004
g = 9.8
vx = v

P = u*m*g*v + (Cres/2)*A*p*(v**2)*vx
print("Potência: ", P)