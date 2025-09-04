import numpy as np
import matplotlib.pyplot as plt 
import math
import time

#Define Initial Conditions and system factors#
y0 = float(input('What is the initial position?\n'))
y0dot = float(input('What is the initial velocity?\n'))
zeta = float(input('What is the zeta value? Note: zeta should be between 0 and 1\n'))
omega0 = float(input('What is the omega0 value?\n'))


omegad = omega0 * math.sqrt(-zeta**2+1)
A = y0
B = (y0dot+zeta*omega0*y0)/omegad
y = []
t = np.linspace(0,20,1000)
y = np.exp(-zeta*omega0*t)*(A*np.cos(omegad*t)+B*np.sin(omegad*t))
plt.plot(t,y)
plt.show()
t2=time.time()