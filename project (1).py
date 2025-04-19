#This project will simulate the dynamic systems by using transfer function in s

# Import the packages needed 
import numpy as np # is used for plotting
from control import * # using propertis in control like tf
import matplotlib.pyplot as plt # using toolbox matlab

# first make a transfer function or G(s) 
# in here we have unity feedback ,so H(s) is equal one
# make a open loop and closed loop transfer function then calculate steady state error 
# plotting all of them in terms of time

# Enter the num and den of G(s)
s = tf('s') # in s
num = list(map(float,input('num=').split())) # numerator in s
den =list(map(float,input('den=').split())) # denumator in s

#feedback transfer function
H = 1 # unity feedback
print('H(s)={}'.format(H))

#open loop transfer function
GH = tf(num,den) # make a open loop tf between G(S) and H(s)
print(f'G(s)=', GH)

#closed loop transfer function(feedback control system)
closed_loop_TF =feedback(GH, H) # make a closed loop tf with feedback function
print(closed_loop_TF)


# plotting responce in t
t = np.arange(0, 20, 0.5)

#axis_one
t, y = step_response(closed_loop_TF, t)
black_line = np.ones(len(t))

plt.figure(1) # make a page
plt.subplot(1,2,1)
plt.plot(t,y,label='unit step input')
plt.xlabel('Time [seconds]')
plt.ylabel('Output')
plt.title('Closed-Loop Step Response')
plt.plot(t,black_line ,'r--' ,color='black' )
plt.grid(True)

start = 0
stop = 20
increment  = 0.5
t = np.arange(start,stop,increment)

# axis_two
u = t
t, y = impulse_response(GH,T=t)
error = u - y

plt.subplot(1,2,2)
plt.plot(t,y,color='red',linewidth=1)
plt.xlabel('Time [second]')
plt.ylabel('Error')
plt.grid(True)

start = 0
stop = 20
increment  = 0.5
t = np.arange(start,stop,increment)
u = (t)
t, y = forced_response(GH,T=t,U=u)
error = t - y
step_on = np.zeros(len(t))

plt.figure(2)
plt.subplot(1,2,1)
plt.plot(t,y,label='unit ramp input')
plt.xlabel('time[seccond]')
plt.ylabel('output')
plt.title('unit ramp')
plt.plot(t,step_on)
plt.grid(True)

plt.subplot(1,2,2)
plt.plot(t, error, color= 'red')
plt.xlabel('time')
plt.ylabel('output')
plt.title('ess')
plt.grid(True)

plt.show()









