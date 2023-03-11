import matplotlib.pyplot as plt
import numpy as np

x=[0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5] #t
y=[0.121,0.997,2.55,6.09,9.31,15.8,17.1,25.5,26.5,38.8,41.9] #s

print("REpresentaçao do grafico")
#plt.plot(x, y,"+")


logx=np.log(x)
logy=np.log(y)
plt.plot(logx, logy)
plt.show()

def grafico(x,y):
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

    print("declive:",m)
    print("ordenada na origem:",b)
    print("rr:",rr)
    print("erro m:",vm)
    print("erro b:",vb)


grafico(logx,logy)  


for i in range(0,len(x)):
    x[i]=x[i]**1.95

grafico(x,y)
plt.plot(x, y)
plt.show()