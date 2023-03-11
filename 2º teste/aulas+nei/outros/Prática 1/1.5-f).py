import numpy as np
import matplotlib.pyplot as plt

L = np.array([222.0, 207.5, 194.0, 171.5, 153.0, 133.0, 113.0, 92.0])
X = np.array([2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0])

x = L
y = X

def regressao_linear(x, y):
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
    
    return m, b

plt.scatter(L,X)
plt.xlabel("L (cm)")
plt.ylabel("X (cm)")

resultado_regressao = regressao_linear(L,X)
m = resultado_regressao[0]
b = resultado_regressao[1]

x_rl = np.arange(80,240,10)
l_rl = m * x_rl + b

X = np.array([2.3,2.2,2.0,1.8,2.5,1.4,1.2,1.0])

plt.scatter(L,X)
plt.xlabel("L (cm)")
plt.ylabel("X (cm)")

resultado_regressao = regressao_linear(L,X)
m = resultado_regressao[0]
b = resultado_regressao[1]

x_rl = np.arange(80,240,10)
l_rl_new = m * x_rl + b

plt.plot(x_rl, l_rl, "--", label="Ajuste com os pontos originais.")
plt.plot(x_rl, l_rl_new, "--", label="Ajuste com os pontos modificados.")
plt.legend()