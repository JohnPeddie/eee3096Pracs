#!/usr/bin/python
import datetime
import time
import RPi.GPIO as GPIO
import Adafruit_MCP3008 #required library for adc, see prac sheet for how to install adafruit
import pygame

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
masterCode = "L4R4L4"
running = 0
#ADC PINS
SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8


def main():
	global sline,mode,uline,lline,log,dirr,startpoint,lockMode,count,masterCode,running
	state = "locked"
	pause = 0.5
	initPins(sline, mode, uline, lline)
	#initADC()
	GPIO.add_event_detect(sline, GPIO.FALLING, callback=clearHistory, bouncetime=200)
	GPIO.add_event_detect(mode, GPIO.FALLING, callback=toggleMode, bouncetime=200)

	while (1):
		while(running == 0):

			if (lockMode & 1):#odd therefore secure
				#print("Device is now in secure mode")
				#secure
				if (len(log) >=1):


					current = getData()
					if (current > (log[-1] +0.2) or current < (log[-1] -0.2)):

						if (current > log[-1]):

							log.append(current)
							print("left")
							dirr.append("left")
							count = time.time()
						elif (current < log[-1]):

							log.append(current)
							print("right")
							dirr.append("right")
							count = time.time()
					if (time.time()-count > pause):
						print("break")
						dirr.append("break")
					if (time.time()-count >1):
						print("code entered")
						if (directionsToCodeSEC(dirr)==masterCode):
							print("unlocked")
							playSound("enginestart.mp3")
							running = 1

						else:
							print("code incorrect")
							playSound("fail.mp3")
							running =1



			else:
				#print("Device is now in unsecure mode")
				if (len(log) >=1):


					current = getData()
					if (current > (log[-1] +0.2) or current < (log[-1] -0.2)):

						if (current > log[-1]):

							log.append(current)
							print("left")
							dirr.append("left")
							count = time.time()
						elif (current < log[-1]):

							log.append(current)
							print("right")
							dirr.append("right")
							count = time.time()
					if (time.time()-count >1):
						print("code entered")
						if (directionsToCodeUNSEC(dirr)==masterCode):
							print("unlocked")
							playSound("enginestart.mp3")
							running = 1

						else:
							print("code incorrect")
							playSound("fail.mp3")
							running =1

def clearHistory(channel):
	global log,dirr,startpoint,count,running
	print("sline pressed")
	startpoint = getData()
	log = [startpoint]
	dirr = [""]
	count = time.time()
	running = 0



def toggleMode(channel):
	global lockMode
	print("Mode changed")
	lockMode +=1

def playSound(file):
	pygame.init()
	pygame.mixer.init()
	pygame.mixer.music.load(file)
	pygame.mixer.music.play()




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

def directionsToCodeSEC(dirr):
	#['', 'right', 'right', 'right', 'right', 'left', 'left', 'left', 'left', 'right', 'right', 'right', 'right']
	new = dirr[1:]
	new.append("stop")
	c = 0
	start = new[0]
	priv =start
	string = ""

	for i in new:
   		if (priv != i and i != "break"):
			string = string +str(c)
       			c =0
   		if (i == "left" and c ==0):
       			string = string + "L"
   		if (i == "right" and c ==0):
       			string = string + "R"
   		if (i == "left"):
       			c+=1
   		if (i == "right"):
       			c +=1
   		priv = i
	return string

def directionsToCodeUNSEC(dirr):
	return ""


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
