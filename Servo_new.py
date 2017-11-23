import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
servo2 = GPIO.PWM(14,50)
servo3 = GPIO.PWM(15,50)
servo4 = GPIO.PWM(18,50)

initPos2 = 13.0
initPos3 = 9.5
initPos4 = 4.0

finalPos2 = 7.0
finalPos3 = 4.0
finalPos4 = 7.0

servo2.start(initPos2)
servo3.start(initPos3)
servo4.start(initPos4)

while True:
    pos2 = initPos2
    pos3 = initPos3
    pos4 = initPos4

    speed2 = (finalPos2 - initPos2)/100
    speed3 = (finalPos3 - initPos3)/100
    speed4 = (finalPos4 - initPos4)/100

    #stay at initial position for a while
    for i in range(100):
        servo2.ChangeDutyCycle(pos2)
        servo3.ChangeDutyCycle(pos3)
        servo4.ChangeDutyCycle(pos4)
        time.sleep(0.02)

    #start from initial position to final position
    for i in range(100):
        pos3 = pos3 + speed3
        servo3.ChangeDutyCycle(pos3)
        time.sleep(0.02)

    time.sleep(1)

    for i in range(100):
        pos2 = pos2 + speed2
        servo2.ChangeDutyCycle(pos2)
        time.sleep(0.02)
    
    time.sleep(1)

    for i in range(100):
        pos4 = pos4 + speed4
        servo4.ChangeDutyCycle(pos4)
        time.sleep(0.02)

    time.sleep(3)

    #from final position to initial position
    speed2 = (initPos2 - finalPos2)/100
    speed3 = (initPos3 - finalPos3)/100
    speed4 = (initPos4 - finalPos4)/100

    for i in range(100): 
        pos4 = pos4 + speed4
        servo4.ChangeDutyCycle(pos4)
        time.sleep(0.02)

    time.sleep(1)

    for i in range(100): 
        pos2 = pos2 + speed2
        servo2.ChangeDutyCycle(pos2)
        time.sleep(0.02)

    time.sleep(1)
   
    for i in range(100): 
        pos3 = pos3 + speed3
        servo3.ChangeDutyCycle(pos3)
        time.sleep(0.02)


    time.sleep(3)
