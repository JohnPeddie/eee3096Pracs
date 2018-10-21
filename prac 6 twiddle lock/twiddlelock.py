#!/usr/bin/python
import datetime
import time
import RPi.GPIO as GPIO
import Adafruit_MCP3008 #required library for adc, see prac sheet for how to install adafruit

#global varialbles:
sline = 23
mode = 24
lline = 22
uline = 27
lockMode = 0
log=[]
dirr=[]
startpoint = 0
#ADC PINS
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8


def main():
	global sline,mode,uline,lline,log,dirr,startpoint,lockMode
	state = "locked"
	initPins(sline, mode, uline, lline)
	#initADC()
	GPIO.add_event_detect(sline, GPIO.FALLING, callback=clearHistory, bouncetime=200)
	GPIO.add_event_detect(mode, GPIO.FALLING, callback=toggleMode, bouncetime=200)


	while(1):
		if (lockMode & 1):#odd therefore secure
			#print("Device is now in secure mode")
			current = getData()
			if (current > log[len(log)-1]):
				dirr.append("left")
				print("left")
			else:
				dirr.append("Right")
				print("Right")
		else:
			#print("Device is now in unsecure mode")
			print("unsecure")
		time.sleep(1)
def clearHistory(channel):
	global log,dirr,startpoint
	startpoint = getData()
	log = [startpoint]
	dirr = []

def toggleMode(channel):
	global mode
	print("Mode changed")
	mode +=1



def initPins(sline, toggleMode, uline, lline):
	#initialise all the pins
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(sline, GPIO.IN, pull_up_down=GPIO.PUD_UP) #eg of a pin being initialised
	GPIO.setup(mode, GPIO.IN, pull_up_down=GPIO.PUD_UP)
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
