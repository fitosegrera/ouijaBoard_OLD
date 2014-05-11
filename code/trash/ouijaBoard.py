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

GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(25, GPIO.IN)

char = ''
soulName = ''
typeDone = 1
searchState = 0
countH = 0
countI = 0
countT = 0
countL = 0
countE = 0
countR = 0
waiting = 0.2

########################################################
########################################################
while (searchState == 0):

	if(GPIO.input(4) ==1):
		print('OUIJA')
		countOuija = countOuija + 1
		if countOuija == 1:
			print soulName
			countOuija = 0
			time.sleep(waiting)
			searchState = 1

	if(GPIO.input(17) == 1):
		print('H')
		char = 'H'
		countH = countH + 1
		if countH == 1:
			soulName = soulName + char;
			print soulName
			countH = 0
			time.sleep(waiting)

	if(GPIO.input(18) ==1):
		print('I')
		char = 'I'
		countI = countI + 1
		if countI == 1:
			soulName = soulName + char;
			print soulName
			countI = 0
			time.sleep(waiting)

	if(GPIO.input(27) == 1):
		print('T')
		char = 'T'
		countT = countT + 1
		if countT == 1:
			soulName = soulName + char;
			print soulName
			countT = 0
			time.sleep(waiting)

	if(GPIO.input(22) ==1):
		print('L')
		char = 'L'
		countL = countL + 1
		if countL == 1:
			soulName = soulName + char;
			print soulName
			countL = 0
			time.sleep(waiting)

	if(GPIO.input(23) == 1):
		print('E')
		char = 'E'
		countE = countE + 1
		if countE == 1:
			soulName = soulName + char;
			print soulName
			countE = 0
			time.sleep(waiting)

	if(GPIO.input(25) == 1):
		print('R')
		char = 'R'
		countR = countR + 1
		if countR == 1:
			soulName = soulName + char;
			print soulName
			countR = 0
			time.sleep(waiting)			

GPIO.cleanup()

########################################################
########################################################

if searchState == 1:
	
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

	
