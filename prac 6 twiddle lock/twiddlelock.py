#!/usr/bin/python
import datetime
import time
import RPi.GPIO as GPIO
import Adafruit_MCP3008 #required library for adc, see prac sheet for how to install adafruit

#global varialbles:
sline = 23
toggleMode = 24
lline = 22
uline = 27
mode = 0
log=[]
dir=[]

#ADC PINS
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8


def main():
	global sline,toggleMode,uline,lline,log,dir
	state = "locked"
	initPins(sline, toggleMode, uline, lline)
	#initADC()
	GPIO.add_event_detect(sline, GPIO.FALLING, callback=clearHistory, bouncetime=200)
	GPIO.add_event_detect(toggleMode, GPIO.FALLING, callback=toggleMode, bouncetime=200)


	while(1):
		print(getData())
		time.sleep(1)
		#if (mode & 1):#odd therefore secure
			#do secure stuff
		#else:
			#do unsecure stuff
			#adc turns
			#log.append(adcTime)
			#dir.append(Adcdirection)

def clearHistory(channel):
	global log,dir
	log = []
	dir = []

def toggleMode(channel):
	global mode
	mode +=1



def initPins(sline, toggleMode, uline, lline):
	#initialise all the pins
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(sline, GPIO.IN, pull_up_down=GPIO.PUD_UP) #eg of a pin being initialised
	GPIO.setup(toggleMode, GPIO.IN, pull_up_down=GPIO.PUD_UP)
	GPIO.setup(lline, GPIO.OUT)
	GPIO.setup(uline, GPIO.OUT)
	print("Pins initialised")

def getData():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(SPIMOSI, GPIO.OUT)
        GPIO.setup(SPIMISO, GPIO.IN)
        GPIO.setup(SPICLK, GPIO.OUT)
        GPIO.setup(SPICS, GPIO.OUT)
	mcp = Adafruit_MCP3008.MCP3008(clk=SPICLK, cs=SPICS, mosi=SPIMOSI, miso=SPIMISO)

	pot_adc = mcp.read_adc(0)
	potV = round((pot_adc/1024.0)*3.3, 2)



	return potV


def Sort(combination):
    for i in range(len(combination)):
        pos = i

        for j in range(i+1, len(combination)):
            if combination[pos] > combination[j]:
                pos = j

        temp = combination[i] #temp variable to store the element that needs to be swapped
        combination[i] = combination[pos]
        combination[pos] = temp

    return combination

if __name__ == '__main__':
	main()
