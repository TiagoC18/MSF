import numpy as np
import matplotlib.pyplot as plt
import math
x=np.array([0.00, 0.735, 1.363, 1.739, 2.805, 3.814, 4.458, 4.995, 5.666, 6.329])
y=np.array([0, 1, 2, 3,4, 5, 6, 7, 8, 9])
m, b = np.polyfit(x, y, 1)
plt.scatter(x,y)
plt.plot(x, m*x + b)
plt.scatter(np.log(x), np.log(y))
plt.plot(np.log(x),m*np.log(x)+b)
sx=0
sy=0
s=0
sx2=0
sy2=0
N=10
for i in range (len(x)):
    sx+= x[i]
    sy+= y[i]
    s+= (x[i]*y[i])
    sx2+= x[i]**2
    sy2+= y[i]**2
    vm=sx/len(x)
r=(((N*s)-(sx*sy))**2)/(((N*sx2)-(sx**2))*((N*sy2)-(sy**2)))
dm=(abs(m))*((((1/r)-1)/(N-2))**0.5)
db= dm*((sx2/N)**0.5)
#print("x=", sx)
#print("y=", sy)
#print("xy=", round(s, 2))
#print("x**2=", sx2)
#print("y**2=", round(sy2, 3))
print("m=", round(m, 9))
print("b=", round(b, 9))
print("r**2=", round(r,9)) #coeficiente de determinação (próximo de 1 é bom ajuste, próximo de 0 indica que o modelo não é linear)
print("dm=", round(dm, 9)) #erros que afetam o declive (m)
print("db=", round(db, 9)) #erros que afetam a ordenada na origem (b)


plt.show()



#a) Não