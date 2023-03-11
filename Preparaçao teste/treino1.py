import matplotlib.pyplot as plt
import numpy as np

x=[0.15,0.20,0.16,0.11,0.25,0.32,0.40,0.45,0.50,.55] #M
y=[1.21,1.4,1.26,1.05,1.6,1.78,2,2.11,2.22,2.33] #T

print("REpresentaçao do grafico")
#plt.plot(x, y,)

logx=np.log(x)
logy=np.log(y)
#plt.plot(logx, logy,"o")

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



for i in range(0,len(y)):
    y[i]=y[i]**2

print("REpresentaçao do grafico")
plt.plot(x, y,"o")
plt.show()
grafico(x,y)
