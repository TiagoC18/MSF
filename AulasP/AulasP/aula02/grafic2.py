import numpy as np
import matplotlib.pyplot as plt
x=np.array([222.0, 207.5, 194.0, 171.5, 153.0, 133.0, 113.0, 92.0])
y=np.array([2.3, 2.2, 2.0, 1.8, 1.6, 1.4, 1.2, 1.0])
m, b = np.polyfit(x, y, 1)
plt.scatter(x,y)
plt.plot(x, m*x + b)

sx=0
sy=0
s=0
sx2=0
sy2=0
N=7

for i in range (len(x)):
    sx+= x[i]
    sy+= y[i]
    s+= (x[i]*y[i])
    sx2+= x[i]**2
    sy2+= y[i]**2
r=(((N*s)-(sx*sy))**2)/(((N*sx2)-(sx**2))*((N*sy2)-(sy**2)))
dm=(abs(m))*((((1/r)-1)/(N-2))**0.5)
db= dm*((sx2/N)**0.5)
print("x=", sx)
print("y=", sy)
print("xy=", round(s, 2))
print("x**2=", sx2)
print("y**2=", round(sy2, 3))
print("m=", round(m, 9))
print("b=", round(b, 9))
print("r**2=", round(r,9))
print("dm=", round(dm, 9))
print("db=", round(db, 9))

plt.show()

