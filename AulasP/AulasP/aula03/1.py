import matplotlib.pyplot as plt
import numpy as np

va=70
va=va/3.6
a=2.0
lmA=np.linspace(0,100,10)
x=va*lmA
plt.plot(lmA,x)

thatsthesoundofthapolice= np.linspace(0,100,10)
t=thatsthesoundofthapolice
police=(1/2)*a*(t**2)
plt.plot(thatsthesoundofthapolice, police)
plt.show()
tencontro=(2*va)/a
xencontro=va*tencontro
print('tempo de encontro:', tencontro)
print('encontram-se em', xencontro)
