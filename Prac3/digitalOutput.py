#!/usr/bin/python
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # use GPIO pin numbering
# may change to GPIO.BOARD phy.pin if preferred
pinnumber = 22 # set pinnumber to pin 22
second = 1
GPIO.setup(pinnumber, GPIO.OUT) # set pin pinnumber as digital output
GPIO.output(pinnumber, GPIO.LOW) # set pin pinnumber default low
GPIO.output(pinnumber, True) # set pin pinnumber output high
time.sleep(second) # delay for second
GPIO.output (pinnumber, False) # set pin pinnumber output low
time.sleep(second) # delay for second
GPIO.cleanup() # release GPIO pins from its opeartion
