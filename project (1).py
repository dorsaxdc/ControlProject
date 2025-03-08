import numpy as np
import control
import matplotlib.pyplot as plt
from spb import plot_impulse_response
from numpy import exp
#unit ramp response curve for GH

# for TransferFunction
s = control.tf(' s ')
num = list(map(float,np.array(input('num = ').split())))
den =list(map(float,np.array(input(' den= ').split())))
control.tf(num, den)
GH = control.tf(num,den)
print('G(s) = ', GH)

H = 1 
print('H(s) = ', H)

#closed loop transfer function
closed_loop_TF =control.feedback(GH,H)
print('closed_loop_TF = ', closed_loop_TF)

start = 0
stop = 20
increment  = 0.5
t = np.arange(start,stop,increment)
t, y = control.step_response(closed_loop_TF, t)
step_in = 1*np.ones(len(t))

plt.figure(1)
plt.subplot(1,2,1)
plt.plot(t,y,label='unit step input')
plt.xlabel('Time [seconds]')
plt.ylabel('Output')
plt.title('Closed-Loop Step Response')
plt.plot(t,step_in,'r--',color='black')
plt.legend()
plt.grid(True)

error = abs(1 - y[-1])
t,error = control.impulse_response(GH,t)
print(error)

plt.subplot(1,2,2)
plt.plot(t,error,color='red',linewidth=1)
plt.xlabel('Time [second]')
plt.ylabel('Error')
plt.legend()
plt.grid(True)

start = 0
stop = 20
increment  = 0.5
t = np.arange(start,stop,increment)
u = t
t, y = control.forced_response(GH,T=t,U=u)
error = u - y

plt.figure(2)
plt.subplot(1,2,1)
plt.plot(t,y,label='unit ramp input')
plt.xlabel('time[seccond]')
plt.ylabel('output')
plt.title('unit ramp')
plt.grid(True)
plt.legend()

plt.subplot(1,2,2)
plt.plot(t, error, color= 'red')
plt.xlabel('time')
plt.ylabel('output')
plt.title('ess')
plt.grid(True)
plt.legend()

plt.show()




