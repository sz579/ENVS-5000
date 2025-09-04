import numpy as np
import matplotlib.pyplot as plt 
import math
import time

#Define Initial Conditions and system factors#
y0 = 0.0
y0dot = 1.0
zeta = 0.5
omega0 = 1.0


omegad = omega0 * math.sqrt(-zeta**2+1)
A = y0
B = (y0dot+zeta*omega0*y0)/omegad
y = []

t = np.linspace(0,20,1000)
t1 = time.time()
for i in range(0,1000,1):
    y.append(math.exp(-zeta*omega0*t[i])*(A*math.cos(omegad*t[i])+B*math.sin(omegad*t[i])))

plt.plot(t,y)
plt.show()
t2 = time.time()
print(t2-t1)

y = []
t1=time.time()
y = np.exp(-zeta*omega0*t)*(A*np.cos(omegad*t)+B*np.sin(omegad*t))
plt.plot(t,y)
plt.show()
t2=time.time()
print(t2-t1)