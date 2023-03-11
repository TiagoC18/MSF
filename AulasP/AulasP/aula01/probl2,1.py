import numpy as np
import matplotlib.pyplot as plt

va=70 #km/h
va=va/3.6 #m/s
a=2.0

lmA=np.linspace(0,22,1000)    #tempo carro A
t=lmA
xat=va*t                    #xa(T)=va*T velovidade constante logo va=70
plt.plot(lmA,xat)
                                       #tempo carro A
t=lmA
policiaYxp=(1/2)*a*(t**2)                  #xa(T)=1/2*a*t**2 acelaraçao constante logo a=2.0
plt.plot(t,policiaYxp)
plt.show()

tencontro=(2*va)/a
xencontro=va*tencontro
print('tempo de encontro= ',tencontro)
print('X de encontro= ',xencontro)


