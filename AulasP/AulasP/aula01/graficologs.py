import matplotlib.pyplot as plt
import numpy

x=[200,300,400,500,600,700,800,900,1000,1100]#massa
y=[0.6950,4.363,15.53,38.74,75.08,125.2,257.9,344.1,557.4,690.7] #T

plt.plot(x,y)
plt.show()
print("Nao é linear")

logx=numpy.log(x)
logy=numpy.log(y)

plt.plot(logx,logy)
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
 
 #y=c*(x**m)        m= declive

grafico(logx,logy)