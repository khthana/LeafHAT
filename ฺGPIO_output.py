import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
while True:
    GPIO.output(5,0)
    print('GPIO=OFF')
    time.sleep(1)
    GPIO.output(5,1)
    print('GPIO=ON')
    time.sleep(1)
