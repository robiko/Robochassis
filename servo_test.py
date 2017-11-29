import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
servo2 = GPIO.PWM(16,50)
servo3 = GPIO.PWM(20,50)
servo4 = GPIO.PWM(21,50)

initPos2 = 3.0
initPos3 = 4.0
initPos4 = 7.5

midPos2 = 8.5
midPos3 = 9.0 
midPos4 = 11.0

finalPos2 = 3.0
finalPos3 = 4.0
finalPos4 = 9.0

speed = 0.02

servo2.start(initPos2)
servo3.start(initPos3)
servo4.start(initPos4)


if __name__ == '__main__':
    try:
        while True:
           servo2.ChangeDutyCycle(initPos2)
           servo3.ChangeDutyCycle(initPos3)
           servo4.ChangeDutyCycle(initPos4)
           time.sleep(2)

           n = int( abs((midPos3 - initPos3)/speed) )
           for i in range(n):
               pos3 =  initPos3 + float(i)*speed
               servo3.ChangeDutyCycle(pos3)
               time.sleep(0.02)
           n = int( abs((midPos2 - initPos2)/speed) )
           for i in range(n):
               pos2 = initPos2 + float(i)*speed
               servo2.ChangeDutyCycle(pos2)
               time.sleep(0.02)
           n = int( abs((midPos4 - initPos4)/speed) )
           for i in range(n):
               pos4 = initPos4 + float(i)*speed
               servo4.ChangeDutyCycle(pos4)
               time.sleep(0.02)
 
           time.sleep(2)

           n = int(abs((finalPos4 - midPos4)/speed) )
           for i in range(n):
               pos4 = midPos4 - float(i)*speed
               servo4.ChangeDutyCycle(pos4)
               time.sleep(0.02)
           n = int(abs((finalPos2 - midPos2)/speed) )
           for i in range(n):
               pos2 = midPos2 - float(i)*speed
               servo2.ChangeDutyCycle(pos2)
               time.sleep(0.02)
           n = int(abs((finalPos3 - midPos3)/speed) )
           for i in range(n):
               pos3 = midPos3 - float(i)*speed
               servo3.ChangeDutyCycle(pos3)
               time.sleep(0.02)
  
           time.sleep(2)

    except KeyboardInterrupt:
        print('Program stopped by user')
        GPIO.cleanup()
