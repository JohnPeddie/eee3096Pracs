#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
buttonOn=23
buttonBright=24
buttonDim=27
led=22
brightness = 0
brightnessLow=7
f= 100
dutycycle = 100

def downBrightness():
	global brightnessLow

        if brightnessLow > 0:
		print("Lowered brightness")
                brightnessLow-=1
        else:
		print("reset brightness")
                brightnessLow = 7
        ds = (brightnessLow*10)
        print("Changing Duty cyle to "+ str(ds))
        PWM.ChangeDutyCycle(ds)
def upBrightness():
        global brightness

        if brightness < 10:
		print("Upped brightness")
                brightness+=1
        else:
		print("Reset brightness")
                brightness =0
        ds = (brightness*10)
        print("Changing Duty cyle to "+ str(ds))
        PWM.ChangeDutyCycle(ds)

GPIO.setup(buttonOn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonBright, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonDim, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led, GPIO.OUT)
PWM = GPIO.PWM(led, f)
GPIO.output(led, GPIO.LOW)
state = False
while True:
    PWM.start(0)
    input_state = GPIO.input(buttonOn)
    if input_state == False:
        print('Turning On')
	state = True
        PWM.start(100)
	time.sleep(0.2)
    while state == True:	
		
        inBright = GPIO.input(buttonBright)
	if inBright == False:
		upBrightness()
		time.sleep(0.2)
	inDim = GPIO.input(buttonDim)
        if inDim == False:
                downBrightness()
                time.sleep(0.2)
	input_state= GPIO.input(buttonOn)
	if input_state == False:
		print("Switching Off")
		state = False
		time.sleep(0.2)
		break

