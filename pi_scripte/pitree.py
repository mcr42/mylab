import time
import random
import RPi.GPIO as GPIO

TIME=0.05
SEQ=(1,1,1,1,1,1,1,1,1,1,1,1,1,100,100,1)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False);

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)


p1 = GPIO.PWM(3, 50)  # channel=12 frequency=50Hz
p2 = GPIO.PWM(5, 50)
p3 = GPIO.PWM(7, 50)
p4 = GPIO.PWM(11, 50)
p5 = GPIO.PWM(13, 50)
p6 = GPIO.PWM(15, 50)
p7 = GPIO.PWM(19, 50)
p8 = GPIO.PWM(21, 50)
p9 = GPIO.PWM(23, 50)
p10 = GPIO.PWM(8, 50)
p11 = GPIO.PWM(10, 50)
p12 = GPIO.PWM(12, 50)
p13 = GPIO.PWM(16, 50)
p14 = GPIO.PWM(18, 50)
p15 = GPIO.PWM(22, 50)
p16 = GPIO.PWM(24, 50)
p17 = GPIO.PWM(26, 50)

p1.start(0)
p2.start(0)
p3.start(0)
p4.start(0)
p5.start(0)
p6.start(0)
p7.start(0)
p8.start(0)
p9.start(0)
p10.start(0)
p11.start(0)
p12.start(0)
p13.start(0)
p14.start(0)
p15.start(0)
p16.start(0)
p17.start(0)




try:
    while 1:
#        for dc in range(0, 100, 5):
            dc=random.choice(SEQ)
            p1.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p2.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p3.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p4.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p5.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p14.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p15.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p16.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p6.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p7.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p8.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p9.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p10.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p11.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p12.ChangeDutyCycle(dc)
            dc=random.choice(SEQ)
            p13.ChangeDutyCycle(dc) 
            dc=random.choice(SEQ)
            p17.ChangeDutyCycle(dc) 
            
                        
            time.sleep(TIME)
 
except KeyboardInterrupt:
    pass
#p.stop()
GPIO.cleanup()
