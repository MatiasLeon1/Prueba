# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 09:21:44 2020

@author: Matias
"""

#Hablar de 3 cosas hoy:
    #1 como se va a ejecutar el codigo.
    #2 Integracion d EDOs por Euler (metodo mas charcha que existe)
    #3 [video] Correcciones adicionales (mas impacto en el codigo)

# FJ2/FJ3 fuerzas adicionales a la gravedad, bajan error de miles de metros
#a cientos de metros. Tambien se puede sumar la fuerza de arrastre.


"""
#1 
#Como recibir un parametro de entrada en mi codigo.
import sys #me permite interactuar con el S. Operativo

argc = len(sys.argv) #argument count

if argc ==1:
    nombre = "Elon"
else:
    nombre = sys.argv[1]
    
print(f"Hola {nombre}!")

print(f"sys.argv[0] = {sys.argv[0]}") #Imprime ubicacion del archivo
"""
#2
from scipy.integrate import odeint
import numpy as np
import matplotlib.pylab as plt

a = 2.

# z" = a*z
def zp(z,t):
    return a*z

def eulerint(zp,z0,t,Nsub=1):
    Nt = len(t)
    Ndim = len(np.array([z0]))
    
    z = np.zeros((Nt,Ndim))
    z[0,:]=z0
    
    #z(i+1)=zp:i*dt+z_i
    for i in range(1,Nt):
        t_anterior = t[i-1]
        dt = (t[i]-t[i-1])/Nsub
        z_temp = z[i-1,:].copy() #o *1.0
        for k in range(Nsub):
            z_temp+= dt*zp(z_temp,t_anterior+k*dt)
        z[i,:]=z_temp
          
    return z

z0 = 1.
t = np.linspace(0,2,100)


z_odeint = odeint(zp,z0,t)
z_real = z0*np.exp(a*t)
z_euler = eulerint(zp,z0,t,Nsub=1)

plt.plot(t,z_odeint,label="odeint")
plt.plot(t,z_euler,label="eulerint")
plt.plot(t,z_real,label="real")
plt.legend()
plt.show()

Le agrego cuañqiuier mierda