import matplotlib.pyplot as plt

x=[222.0,207.5,194.0,171.5,153.0,133.0,113.0,92.0] #L
y=[2.3,2.2,2.0,1.8,1.6,1.4,1.2,1.0] #X

print("REpresentaçao do grafico")
plt.plot(x, y,'o')
plt.show()

print()
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
print("")
print("A reta do grafico é igual a y=",m,"x+",b)
print("o declive é igual a m=",m,"+",vm)
print("a ordenada é igual a b=",b,"+",vb)
print()
ord=[]
for i in x:
    ord.append(((i*m)+b))

plt.plot(x, ord,'x')
plt.show()
L=165.0
X=(m*L)+b
print("O valr de x quando l=",L," é igual a ",X)