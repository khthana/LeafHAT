import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

input_pin = 13

GPIO.setup(input_pin, GPIO.IN)

while True:
    state = GPIO.input(input_pin)
    print(state)
    time.sleep(1)
