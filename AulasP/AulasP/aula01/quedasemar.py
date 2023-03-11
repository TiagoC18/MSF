# Queda sem resistência do ar
# Integração numérica de dx/dt = vx, pelo Método de Euler
import numpy as np
import matplotlib.pyplot as plt

dt=0.01
tf=4.0
t0=0
x0=0
v0x=0
g=9.80

n=np.int((tf-t0)/dt+0.1)
print('n',n)

t=np.zeros(n+1)                               # n+1 elementos; último índice n
x=np.zeros(n+1)
vx=np.zeros(n+1)
vx[0]=v0x
t[0]=t0
x[0]=x0

for i in range(n):                          # Método de Euler (n elementos)
    t[i+1]=t[i]+dt
    vx[i]=g*t[i]
    x[i+1]=x[i]+vx[i]*dt                    # último x[n]= x[n-1]+vx[n-1]*dt
                                            # índice n : é o (n+1)o elemento

plt.scatter(t,x)
plt.show()