import matplotlib.pyplot as plt
import numpy

y=[9.676 , 6.355, 4.261, 2.729, 1.862, 1.184, 0.7680, 0.4883, 0.3461, 0.2119] #atividade
x= [c * 5 for c in range(0, len(y))]#tempo

plt.plot(x,y)
plt.show()

logy=numpy.log(y)

plt.plot(x,logy)
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


grafico(x,logy)