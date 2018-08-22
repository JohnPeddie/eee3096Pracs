#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
pin = 23
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(pin)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
GPIO.cleanup() # release GPIO pins from its opeartion
