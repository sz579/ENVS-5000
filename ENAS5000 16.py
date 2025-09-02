import numpy as np
import matplotlib.pyplot as plt
import math


timetotemp = lambda t: math.exp(-(math.log(30/28))/10*t)*30+60

temptotime = lambda T: math.log(30/(T-60))/(math.log(30/28)/10)

t=np.linspace(0,1000,10000)
T=[]
for i in range(0,10000,1):
    T.append(timetotemp(t[i]))

while 1:
    try:
        time_input=input('How many minutes of the data do you want?\nType \'exit\' to quit\n')
        if time_input == 'exit':
            break
        time_input = int(time_input)
        if time_input < 0:
            raise ValueError('input must be positive integer!')
        if time_input >=0:
            plt.plot(t,T,'b')
            plt.plot(t,np.linspace(60,60,10000),':b')
            plt.plot(time_input,timetotemp(time_input),'o:r')
            plt.plot([time_input,time_input],[60,timetotemp(time_input)],':r')
            plt.plot([0,time_input],[timetotemp(time_input),timetotemp(time_input)],':r')
            plt.xlabel('time/min')
            plt.ylabel('Temperature/F')
            plt.title('Temperature - Time graph')
            plt.show()
            print('The temperature is',timetotemp(time_input),'F\n')
    except ValueError:
        print('Wrong Input!')
    plt.cla()
print('Successfully Exit!')
