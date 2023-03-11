import numpy as np

y0 = 20
g = 9.8
vT = 6.80

t = np.arccosh(10**(y0*g/vT**2))*vT/g

print("Resitência do ar:", t, "segundos.")

ts = np.sqrt(2*y0/g)

print("Sem resistencia do ar:", ts, "segundos.")