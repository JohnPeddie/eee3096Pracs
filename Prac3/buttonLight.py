#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
buttonOn=23
buttonBright=24
buttonDim=27
led=22
GPIO.setup(buttonOn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, GPIO.LOW)

while True:
    input_state = GPIO.input(buttonOn)
    if input_state == False:
        print('Button Pressed')
	GPIO.output(led, True)
        time.sleep(0.2)
	GPIO.output (led, False)
