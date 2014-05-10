#              _ _         _                         _ 
#             (_|_)       | |                       | |
#   ___  _   _ _ _  __ _  | |__   ___   __ _ _ __ __| |
#  / _ \| | | | | |/ _` | | '_ \ / _ \ / _` | '__/ _` |
# | (_) | |_| | | | (_| | | |_) | (_) | (_| | | | (_| |
#  \___/ \__,_|_| |\__,_| |_.__/ \___/ \__,_|_|  \__,_|
#              _/ |                                    
#             |__/                                     
#
#Ouija Board
#Code for controlling the ouija board (raspberry pi digital pins) and Google Search API
#fito_segrera / fii.to
#started 05-07-14

import RPi.GPIO as GPIO
import time
import urllib
import json as m_json

########################################################################################
#When the board is turned ON it sets the position of the XY pointer to 0,0 coordinate...

########################################################################################
#listen for any switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

char = ''
soulName = ''
typeDone = 1
debugCounter = 0

while (typeDone == 1):
	if (GPIO.input(23) == 1):
		print("Button1 PRESSED")
		char = 'a'
		debugCounter = debugCounter + 1
		print debugCounter
		soulName = soulName + char;
		print soulName
		time.sleep(0.2)
		
	if (GPIO.input(24) == 0):
		print("Button2 PRESSED")
		char = 'b'
		debugCounter = debugCounter + 1
		print debugCounter
		soulName = soulName + char;
		print soulName
		time.sleep(0.2)
	if debugCounter == 4:
		typeDone = 0
	
GPIO.cleanup()


if debugCounter == 4:
	
	########################################################################################
	#wait for the name of the soul to be invoked and search it using the GOOGLE SEARCH API
	countSoulName = 0
	print "////////////////////////////////////////////////////"
	print "The name of the soul is: " + soulName 
	print "////////////////////////////////////////////////////"
	soulName = urllib.urlencode ( { 'q' : soulName } )
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + soulName ).read()
	jsonSoulName = m_json.loads ( response )
	results = jsonSoulName [ 'responseData' ] [ 'results' ]
	for result in results:
		url = result['url']   # for every url object count +1
		countSoulName = countSoulName + 1

	#Check is nothing was found...
	if countSoulName == 0:
		print "THE SOUL IS NOT AVAILABLE"
	else:
		print "HELLO IM HERE"

	
