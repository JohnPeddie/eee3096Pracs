import RPi.GPIO as GPIO
import Adafruit_MCP3008 #required library for adc, see prac sheet for how to install adafruit
import time

def initPins(resetSwitch, frequencySwitch, stopSwitch, displaySwitch):
	#initialise all the pins
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(resetSwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP) #eg of a pin being initialised
	GPIO.setup(frequencySwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(stopSwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(displaySwitch, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	print("Pin initialised")
