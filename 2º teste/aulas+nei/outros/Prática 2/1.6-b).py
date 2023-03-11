import numpy as np
import matplotlib.pyplot as plt

T = np.arange(0, 10, 1)
D = np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.955, 5.666, 6.329])

x = T
y = D
npontos = x.size

xy = x*y
xx = x**2
yy = y**2

sx = x.sum()
sy = y.sum()
sxy = xy.sum()
sxx = xx.sum()
syy = yy.sum()

n = npontos
m = (n*sxy - sx*sy)/(n*sxx - sx**2)
b = (sxx*sy - sx*sxy)/(n*sxx - sx**2)
r2 = (n*sxy - sx*sy)**2/((n*sxx - sx**2)*(n*syy - sy**2))
dm = abs(m) * (np.sqrt((1/r2 - 1)/(n-2)))
db = dm * np.sqrt(sxx/n)

print("m = ", m, "+/-", dm)
print("b = ", b, "+/-", db)
print("r2 = ", r2)