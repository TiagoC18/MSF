import matplotlib.pyplot as plt
import numpy

x=[0,1,2,3,4,5,6,7,8,9]#m
y=[0.00,0.735,1.363,1.739,2.805,3.814,4.458,4.955,5.666,6.329] #km

plt.plot(x,y,"o")
plt.xlabel("Minutos")
plt.ylabel("KM")
#plt.show()

sx=sum(x)
sy=sum(y)
z=[]
xx=[]
yy=[]
a=len(x)
b=0
while b!=a:
    z.append((x[b]*y[b]))
    b=b+1
sxy=sum(z)
b=0
while b!=a:
    xx.append((x[b]**2))
    b=b+1
N=len(x)
b=0
sxx=sum(xx)
while b!=a:
    yy.append((y[b]**2))
    b=b+1
syy=sum(yy)
m=((N*sxy)-(sx*sy))/((N*sxx)-(sx**2))
b=((sxx*sy)-(sx*sxy))/((N*sxx)-(sx**2))
rr=(((N*sxy)-(sx*sy))**2)/(((N*sxx)-(sx**2))*((N*syy)-(sy**2)))
vm=m*((((1/rr)-1)/(N-2))**(1/2))
vb=vm*((sxx/N)**(1/2))
print("O declive é igual a m=", m,"+",vm)
print("A ordenada é igual a b=",b,"x",vb)
print("O coefeciente de correlagaçao é igual a r^2=", rr)
ord=[]
for i in x:
    ord.append(((i*m)+b))

plt.plot(x, ord,'x')
plt.show()

vm= 6.329/9
vmkm=vm*60
print("vm:",vm,"km/m e pelo declive da reta ", m)
print("vm=",vmkm,"km/h")


