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
dirr=[""]
startpoint = 0
count = time.time()
#ADC PINS
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8


def main():
	global sline,mode,uline,lline,log,dirr,startpoint,lockMode,count
	state = "locked"
	initPins(sline, mode, uline, lline)
	#initADC()
	GPIO.add_event_detect(sline, GPIO.FALLING, callback=clearHistory, bouncetime=200)
	GPIO.add_event_detect(mode, GPIO.FALLING, callback=toggleMode, bouncetime=200)


	while(1):

		if (lockMode & 1):#odd therefore secure
			#print("Device is now in secure mode")

			if (len(log) >=1):


				current = getData()
				if (current > log[-1] +0.2 or current < log[-1] -0.2):

					if (current > log[-1]):

						
						print("left")
						dirr.append("left")
						count = time.time()
					elif (current < log[-1]):

						
						print("right")
						dirr.append("right")
						count = time.time()
				if (time.time()-count >1):
					print("code entered")
					print(dirr)
					clearHistory(0)

		else:
			#print("Device is now in unsecure mode")
			print("unsecure")

def clearHistory(channel):
	global log,dirr,startpoint,count
	print("sline pressed")
	startpoint = getData()
	log = [startpoint]
	dirr = [""]
	count = time.time()

	
	
def toggleMode(channel):
	global lockMode
	print("Mode changed")
	lockMode +=1



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
