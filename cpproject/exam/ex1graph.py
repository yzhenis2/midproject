#Graphing
#using the ADC0831 to measure Voltage of 9v battery
#Yelaman Zhenis
#2/4/19



import matplotlib.pyplot as plt
import numpy as np
#define data arrays
time_data=[]
temp_data=[]
#read in the data
lines= np.loadtxt('exam1.txt',delimiter=',')
for line in lines:
    time_data.append(line[0]/3600)#the first item in row is the time
    temp_data.append(line[1])#the 2nd item in row in the temp
#exponential decay function

#have to do the following to use the time data in the exponential function
fit_time_data=np.array(time_data)

#make a plot
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
#make an xy scatter plot
plt.scatter(time_data,temp_data,color='red', label='data')
#add the exp curve w/ guess for consts a and b:


#label the axes etc
ax.set_xlabel('Time(hr)')
ax.set_ylabel('Voltage(V)')
ax.set_title('9V Battery Voltage Continuous discharge')
plt.savefig('ex1.png')
    
