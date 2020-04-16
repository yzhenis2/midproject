#Graphing
#using the ADC0831 to measure Voltage of 9v battery
#Yelaman Zhenis
import matplotlib.pyplot as plt
import numpy as np
#define data arrays
time_data=[]
volt_data=[]
#read in the data
lines= np.loadtxt('exam1.txt',delimiter=',')
for line in lines:
    time_data.append(line[0]/3600)#the first item in row is the time converted to seconds
    volt_data.append(line[1])#the 2nd item in row is the voltage data
#linear regression function
def my_func(x, a, b):
    return b*x+a
#linear regression slope and addition term calculation for continuous charge 
fit_time_data=np.array(time_data)
fit_volts_data = np.array(volt_data)
x = fit_time_data[153:678]
y = fit_volts_data[153:678]
a0 = (sum(np.square(x))*sum(y)-sum(x*y)*sum(x))/(len(x)*sum(np.square(x))-(sum(\
x))**2)
a1 = (len(x)*sum(x*y) - sum(x)*sum(y))/(len(x)*sum(np.square(x))-(sum(x))**2)
a0 = round(a0,3)
a1 = round(a1,3)
#make a plot                                                                
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
#make an xy scatter plot                                                       
plt.scatter(time_data,volt_data,color='red', label='Recorded Data')
#add the linear regression                                                     
plt.plot(x, my_func(x, a0, a1), color = 'black', label = 'Linear Regression'+'\n'+'y = %.3fx+ %.3f' %(a1,a0))
#label the axes etc
ax.set_xlabel('Time(hr)')
ax.set_ylabel('Voltage(V)')
ax.set_title('9V Battery Voltage Continuous discharge')
plt.legend(loc = 'upper right')
plt.savefig('ex1test.png', dpi = 350)
