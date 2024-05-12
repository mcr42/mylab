#!/bin/python3
#!/bin/python3
import time
import os
from datetime import timedelta, datetime

# apparently rpi.gpio does not support interrupts on a pi4
# please use gpiozero for everything now
from gpiozero import Button

##############################################
# This is the configuration
##############################################
#GPIO to use
COUNTGPIO=21
# number of impulses for a 1 digit increment.
IMP_PER_COUNT=100
# maximum number of pulses per hour
IMP_PER_H_MAX=600
# file to append CSV lines to
CSVFILE='/var/log/gas.csv'
# file to store the last counter, 
# in case of undervoltage or power loss
STATEFILE='/var/cache/gascounter'
##############################################
# end of configuration
##############################################

# bounce delay in seconds
BOUNCE_DELAY=3600 / IMP_PER_H_MAX / 10

#increment for half toggle (we count both edges, down and up)
INCREMENT=1/2/IMP_PER_COUNT

counter=0
lastcount=0
lastCSV=datetime.now() - timedelta(minutes=60)
lastSave=lastCSV

#if set, we read the last value from the storage file
try:
    statf=open(STATEFILE, 'r')
    counter=float(statf.readline())
    statf.close()
except Exception:
    counter=0

lastcount=counter

def write_ctr():
    global lastcount, lastSave

    if (counter > lastcount):
        try:
            os.rename(STATEFILE, STATEFILE+".old")
        except Exception:
            pass
        statf=open(STATEFILE, "w")
        statf.write(format(counter, '.5f')+ "\n")
        statf.close()
        lastcount=counter
        lastSave=datetime.now()

def write_csv():
    global lastCSV
    csvf=open(CSVFILE, "a")
    csvf.write(str(datetime.now()) + ", " + format(counter, '.3f')+"\n")
    csvf.close()
    lastCSV=datetime.now()

def increment():
    global counter
    counter+=INCREMENT
#    print(' Counter is ' + str(round(counter,3)))

print(' Counter is ' + str(counter))
print(' Bounce-Delay is ' + str(round(BOUNCE_DELAY,3)))
print(' Today is ' + str(datetime.now()))

button=Button(21, bounce_time=BOUNCE_DELAY)

button.when_pressed = increment
button.when_released = increment

try:

    while 1:
        time.sleep(5)
        if (datetime.now() - lastCSV >= timedelta(minutes=60)):
            write_csv()
        if (datetime.now() - lastSave >= timedelta(minutes=1)):
            write_ctr()


except KeyboardInterrupt:
    pass
write_ctr()


