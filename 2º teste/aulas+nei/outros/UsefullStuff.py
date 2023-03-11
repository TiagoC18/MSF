#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 10:46:01 2022

@author: bruno
"""
import numpy as np
from matplotlib import pyplot as plt
import sympy as sym
from mpl_toolkits import mplot3d

#funções:
 
#auxiliares:
def prodExt(a,b):
    return (a[1]*b[2]-b[1]*a[2],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
    
#1 dimensão:
  
    
def regLin(x,y): 
    x2=x**2
    y2=y**2
    xy=x*y
    n=x.size

    sx=x.sum()
    sy=y.sum()
    sxy=xy.sum()
    sx2=x2.sum()
    sy2=y2.sum()

    m=(n*sxy-sx*sy)/(n*sx2-(sx**2))
    b=(sx2*sy-sx*sxy)/(n*sx2-(sx**2))
    
    r2n=n*sxy-sx*sy
    r2d1=n*sx2-(sx**2)
    r2d2=n*sy2-(sy**2)
    r2=(r2n**2) / (r2d1*r2d2)
    
    varM=abs(m)*np.sqrt( ((1/r2)-1)/(n-2) )
    varB = varM*np.sqrt(sx2/n)
    return m,b,r2,varM,varB


def getR_1D(r0,v0,dt,n,a):
    v=np.empty(n+1)
    v[0]=v0
    r=np.empty(n+1)
    r[0]=y0
    for i in range(n):
        v[i+1]=v[i]+a*dt
        r[i+1]=r[i]+v[i]*dt
    return r,v

def planoInclinado_1D(x0,v0,n,dt,m,pot=0,teta=0): #supõe-se que o ciclista tenta subir
    x=np.empty(n+1)
    vx=np.empty(n+1)
    ax=np.empty(n+1)
    g=9.8
    
    x[0]=x0
    vx[0]=v0
    ax[0]=0
    
    for i in range(n):
        vv=np.abs(vx[i])
        ax[i]=-g*np.sin(teta) +pot/(m*vx[i])
        vx[i+1]=vx[i]+ax[i]*dt
        x[i+1]=x[i]+vx[i]*dt
    return x,vx,ax

def panoInclinado_atr_1D(x0,v0,n,dt,c_atr,A,m,pot,teta=0): #supõe-se que o cliclista tenta subir
    x=np.empty(n+1)
    vx=np.empty(n+1)
    ax=np.empty(n+1)
    
    g=9.8
    
    x[0]=x0
    vx[0]=v0
    ax[0]=0
    
    for i in range(n):
        vv=np.abs(vx[i])
        f_cic=pot/vx[i]
        ax[i]=-g*np.sin(teta) -c_atr*g*np.cos(teta) +pot/(m*vx[i])
        vx[i+1]=vx[i]+ax[i]*dt
        x[i+1]=x[i]+vx[i]*dt
    return x,vx,ax

def panoInclinado_res_1D(x0,v0,n,dt,c_ar,c_atr,A,m,pot,teta=0): #supõe-se que o ciclista tenta subir
    x=np.empty(n+1)
    vx=np.empty(n+1)
    ax=np.empty(n+1)
    
    p_ar=1.225
    g=9.8
    
    x[0]=x0
    vx[0]=v0
    ax[0]=0
    
    for i in range(n):
        vv=np.abs(vx[i])
        ax[i]=-g*np.sin(teta) -c_atr*g*np.cos(teta) -(0.5*c_ar*A*p_ar*vx[i]*vv)/m + pot/(m*vx[i])
        vx[i+1]=vx[i]+ax[i]*dt
        x[i+1]=x[i]+vx[i]*dt
    return x,vx,ax


#2 dimensões:

    
def getR_2D(r0,v0,a0,dt,n):
    x=np.empty(n+1)
    y=np.empty(n+1)
    vx=np.empty(n+1)
    vy=np.empty(n+1)
    
    x[0]=r0[0]
    y[0]=r0[1]
    vx[0]=v0[0]
    vx[1]=v0[1]
    ax=a0[0]
    ay=a0[1]
    
    for i in range(n):
        vx[i+1]=vx[i]+ax*dt
        vy[i+1]=vy[i]+ay*dt
        x[i+1]=x[i]+vx[i]*dt
        y[i+1]=y[i]+vy[i]*dt
    return (x,y),(vx,vy)

def resAr_2D(r0,v0,n,dt,vt):
    x=np.empty(n+1)
    y=np.empty(n+1)
    vx=np.empty(n+1)
    vy=np.empty(n+1)
    ax=np.empty(n+1)
    ay=np.empty(n+1)
    
    g=9.80
    x[0]=r0[0]
    y[0]=r0[1]
    vx[0]=v0[0]
    vy[0]=v0[1]
    ax[0]=0
    ay[0]=-g
    dres=g/vt**2
    
    for i in range(n):
        vv=np.sqrt(vx[i]**2 +vy[i]**2)

        ax[i+1]=-dres*vv*vx[i]
        ay[i+1]=-g-dres*vv*vy[i]
        
        vx[i+1]=vx[i]+ax[i]*dt
        vy[i+1]=vy[i]+ay[i]*dt
        
        x[i+1]=x[i]+vx[i]*dt
        y[i+1]=y[i]+vy[i]*dt
    return (x,y),(vx,vy),(ax,ay)

#3 dimensões:
    
    
def getR_3D(r0,v0,a0,dt,n):
    x=np.empty(n+1)
    y=np.empty(n+1)
    z=np.empty(n+1)
    vx=np.empty(n+1)
    vy=np.empty(n+1)
    vz=np.empty(n+1)
    
    x[0]=r0[0]
    y[0]=r0[1]
    z[0]=r0[2]
    vx[0]=v0[0]
    vy[0]=v0[1]
    vz[0]=v0[2]
    ax=a0[0]
    ay=a0[1]
    az=a0[2]
    
    for i in range(n):
        vx[i+1]=vx[i]+ax*dt
        vy[i+1]=vy[i]+ay*dt
        x[i+1]=x[i]+vx[i]*dt
        y[i+1]=y[i]+vy[i]*dt
    return (x,y,z),(vx,vy,vz)

def airRes_3D(r0,v0,a0,n,dt,vt):
    x=np.empty(n+1)
    y=np.empty(n+1)
    z=np.empty(n+1)
    vx=np.empty(n+1)
    vy=np.empty(n+1)
    vz=np.empty(n+1)
    ax=np.empty(n+1)
    ay=np.empty(n+1)
    az=np.empty(n+1)
    
    x[0]=r0[0]
    y[0]=r0[1]
    z[0]=r0[2]
    vx[0]=v0[0]
    vy[0]=v0[1]
    vz[0]=v0[2]
    ax[0]=a0[0]
    ay[0]=a0[1]
    az[0]=a0[2]
    g=9.80
    dres=g/vt**2
    
    for i in range(n):
        vv=np.sqrt(vx[i]**2 +vy[i]**2)
        
        ax[i]=a0[0]-dres*vv*vx[i]
        ay[i]=a0[1]-dres*vv*vy[i]
        az[i]=a0[2]-dres*vv*vz[i]
        
        vx[i+1]=vx[i]+ax[i]*dt
        vy[i+1]=vy[i]+ay[i]*dt
        vz[i+1]=vz[i]+az[i]*dt
        
        x[i+1]=x[i]+vx[i]*dt
        y[i+1]=y[i]+vy[i]*dt
        z[i+1]=z[i]+vz[i]*dt
    return (x,y,z),(vx,vy,vz),(ax,ay,az)

def magnus(r0,v0,a0,rot,p_ar,r,n,dt,vt,m):
    g=9.80
    A=np.pi*r**2
    apr=0.5*p_ar*A*r

    x=np.empty(n+1)
    y=np.empty(n+1)
    z=np.empty(n+1)
    
    vx=np.empty(n+1)
    vy=np.empty(n+1)
    vz=np.empty(n+1)
    
    ax=np.empty(n+1)
    ay=np.empty(n+1)
    az=np.empty(n+1)
    
    x[0]=r0[0]
    y[0]=r0[1]
    z[0]=r0[2]
    
    vx[0]=v0[0]
    vy[0]=v0[1]
    vz[0]=v0[2]
    
    ax[0]=a0[0]
    ay[0]=a0[1]
    az[0]=a0[2]
    
    dres=g/vt**2
    for i in range(n):
        vv=np.sqrt(vx[i]**2 +vy[i]**2 +vz[i]**2)
        rot_v=prodExt(rot,(vx[i],vy[i],vz[i]))
        
        mag_x=apr*rot_v[0]/m
        mag_y=apr*rot_v[1]/m
        mag_z=apr*rot_v[2]/m
        
        ax[i+1]=ax[0]-dres*vv*vx[i]+mag_x
        ay[i+1]=ay[0]-dres*vv*vy[i]+mag_y
        az[i+1]=az[0]-dres*vv*vz[i]+mag_z
        
        vx[i+1]=vx[i]+ax[i]*dt
        vy[i+1]=vy[i]+ay[i]*dt
        vz[i+1]=vz[i]+az[i]*dt
        
        x[i+1]=x[i]+vx[i]*dt
        y[i+1]=y[i]+vy[i]*dt
        z[i+1]=z[i]+vz[i]*dt
    return (x,y,z),(vx,vy,vz),(ax,ay,az)






#imports:
#sympy:
#sym.(...) permite usar as funções do math(bom quando não sabemos todos os valores lá dentro)
#resolver equações: sym.solve(equação,variável)(assume-se que equação ==0)
#derivada: sym.diff(equação,variável,grau de derivação (opcional) )
#integração: sym.integrate(equação,variável) (sem constante, infinito é dois lowercase o's)
#criar simbolos: var=sym.Symbol("var") (pode depois ser reutilizada para armazenar o valor concreto, mas não colocar o valor antes do symbol)

#matplotlib:
#plt.scatter(x,y) para pontos
#plt.plot(x,y) para retas
#se quiser legendas, colocar label="(label)" no scatter ou plot e plt.legend() no final
#se quiser mudar a cor, colocar color="(primeira letra da cor)" no scatter ou plot
#colocar plt.show() no final
#plt.xlabel() e plt.ylabel para dar nomes aos eixos

#numpy:
#np.(...) permite usar as funções do math NÃO colocar isto ou math.(...) dentro de solves do sympy, usar sym.(...) em vez disso
#np.abs() para módulo
#np.array([...]) para criar arrays, especialmente bom quando esses valores vão ser processados ou colocados no plt por não precisarem de ciclos for
#criar arrays:
    #(é assim que se escreve) np.arange(i,f,dt)
    #np.linspace(i,f,n) quando queremos array com len=n 
#np.polyfit(x,y,n) para, dado um conjunto de pontos (x;y), arranjar a equação de n grau que (supostamente) mais se aproxima dos pontos
#var = np.empty(n) para criar um vetor vazio com n elementos; melhor que np.zeros porque se algo correr mal, vê-se logo no gráfico
#conversão entre radianos e graus: np.degrees(rad) e np.radians(deg)
#np.round(a,i) arredonda a com i casas decimais









#partes úteis:
    #erro de truncatura (local): desenvolver a série de tailor e ver para que ordem de dt (dt,dt**2,dt**3,...) é que começa a diferir
    #erro de truncatura (acumulado): multiplicar o anterior pelos n passos
    #número de algarismos significativos em resultados: ver variável (medida) com menos algarismos significativos
    #erro: dm(por exemplo) com número de casas decimais igual ao valor "principal"    
    
#tipos de gráficos:
    #(x,y)
    #(log(x),y)
    #(log(x),log(y))
    
#erros:
    #usar o maior: erro de medição(p.e.:entre um tracito e outro da régua) != erro de observação(p.e.:parar um relógio quando chega ao fim)
    #digital: 1 do menor intervalo
    #analógico: 1/2 do menor intervalo
    #erro relativo: abs((d_real-d_medido)/d_real)
    #somar: S=L+P; dS=dL+dP
    #subtrair: S=L-P; dS=dL+dP
    #multiplicar: A=C*L; abs(dA/A)=abs(dC/C)+abs(dL/L) (resolvemos para dA)
    #divisão: A=C/L; abs(dA/A)=abs(dC/C)+abs(dL/L) (resolvemos para dA)
    
#derivadas:
    #derivada total: f(x); df/dx fazer derivada em relação a x, apenas para 1 variável
    #derivada parcial(delta é como um 6 espelhado horizontalmente): f(x;y); (delta)f/(delta)x fazer derivada considerando o x como variáveis e o y (e qualquer outra) como constante
    
#algarismos significativos:
    #começar a contar no primeiro número diferente de 0 e ir até ao primeiro número incerto
    #multiplicação e divisão: número de algarismos significativos igual ao do menor (em valor não em número de algarismos significativos) dos fatores
    #soma e subtração: número de casas decimais igual ao do que tem menos casas decimais
    #usar notação científica para forçar a ter o número certo