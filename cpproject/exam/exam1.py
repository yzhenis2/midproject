#Exam 1
#using the ADC0831 to measure Voltage of the 9V Battery
#Yelaman Zhenis

import RPi.GPIO as GPIO
import time
import numpy

#set ADC0831 pins
CS=29
CLK=31
DO=33

#set Voltage pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(CS, GPIO.OUT)
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DO, GPIO.IN)


#define a function to handle reading adc0831 data
def readADC():
    #set initial binary string as empty
    d=''
    #set the cs pin low(starts conversation)
    GPIO.output(CS, False)
    #setting one clock pulse
    GPIO.output(CLK, False)
    GPIO.output(CLK, True)
    GPIO.output(CLK, False)
    #end clock pulse
    #now to read the data synced to more clock pulses
    for n in range(0,8):#read in 8 bits, 0-7
        #one clock pulse
        GPIO.output(CLK, False)
        GPIO.output(CLK, True)
        GPIO.output(CLK, False)
        #end clock pulse
        #list to the DO pin for a bit
        DO_state=GPIO.input(DO)
        if DO_state==True:
            d=d+'1'
        else:
            d=d+'0'
        #repeat until all bits read
    #set CS pin high(end conversation)
    GPIO.output(CS,True)
    #return the binary data to the user
    return d
#define a function to return voltage
def calc_volts(d):
    #we know voltage is on 0 to 5V scale and
    #adc0831 returns binary numbers w/ integer equivalent
    #values between 0 and 255
    d_int = int(d, 2)
    #It was measured that GPIO has 5.175V out of the RPi
    volts = 5.175 * d_int / 255
    #but the step size is 5v/256 steps=0.02v/step. We need to
    #truncate our voltage value
    #to only display sigfigs
    volts=round(volts,2)
    #Then we apply formula for the voltage divider and solve
    # for V_battery
    v_b=volts*2.01
    v_b=round(v_b,2)
    return v_b

#now main event!
try:
    #create data arrays
    time_data=[]
    voltage_data=[]    
    my_test=True
    start_time=time.time()
    while my_test==True:
        #append time to time_Data
        time_data.append(time.time() - start_time)
        #call our function to read a binary data value
        d=readADC()#this returns the binary data string
        #append our binary data to our array
        voltage_data.append(d)
        #we want to monitor voltage for a few first seconds
        #and see if the program calculates voltage right
        #as chip takes data at that moment
        volts=calc_volts(d)
        print('Current battery voltage: ',volts)
        time.sleep(60)#set it to take data with period of 1 minute
        if volts < 4.8:#if the battery becomes "dead", we can stop colecting data
            my_test=False
            print('I am done collecting data :)')
    #open a data file for writing the same directory as the working program
    file = open('exam1.txt','w')
    for n in range(len(time_data)):
        my_volts = calc_volts(voltage_data[n])
        #write the data as comma delimited
        file.write(str(time_data[n]) + ',' + str(my_volts) + '\n')
    #close the file
    file.close()
except KeyboardInterrupt:
    #here you any code or commands to run before the programexits when you press CTRL+C
    print('you sunk my battleship')
finally:
    GPIO.cleanup()#this ensures a clean exit
