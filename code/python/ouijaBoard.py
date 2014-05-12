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
countTime = 0
countOuija = 0
countH = 0
countI = 0
countT = 0
countL = 0
countE = 0
countR = 0
waiting = 1

########################################################
########################################################
while (searchState == 0):

	if(GPIO.input(4) ==1):
		if countTime <= 1:
			countOuija = countOuija + 1
			if countOuija == 1:
				print('Invoking the soul of ' + soulName + '...')
				countOuija = 0
				time.sleep(waiting)
				searchState = 1
				countH = 0
				countI = 0
				countT = 0
				countL = 0
				countE = 0
				countR = 0
				countTime = 0

	if(GPIO.input(17) == 1):
		if countTime <= 1:
			countH = countH + 1
			if countH == 1:
				print('H')
				char = 'H'
				soulName = soulName + char;
				print soulName
				time.sleep(waiting)
				countOuija = 0
				countI = 0
				countT = 0
				countL = 0
				countE = 0
				countR = 0
				countTime = 0

	if(GPIO.input(18) ==1):
		if countTime <= 1:
			countI = countI + 1
			if countI == 1:
				print('I')
				char = 'I'
				soulName = soulName + char;
				print soulName
				time.sleep(waiting)
				countOuija = 0
				countH = 0
				countT = 0
				countL = 0
				countE = 0
				countR = 0
				countTime = 0

	if(GPIO.input(27) == 1):
		if countTime <= 1:
			countT = countT + 1
			if countT == 1:
				print('T')
				char = 'T'
				soulName = soulName + char;
				print soulName
				time.sleep(waiting)
				countOuija = 0
				countH = 0
				countI = 0
				countL = 0
				countE = 0
				countR = 0
				countTime = 0

	if(GPIO.input(22) ==1):
		if countTime <= 1:
			countL = countL + 1
			if countL == 1:
				print('L')
				char = 'L'
				soulName = soulName + char;
				print soulName
				time.sleep(waiting)
				countOuija = 0
				countH = 0
				countI = 0
				countT = 0
				countE = 0
				countR = 0
				countTime = 0

	if(GPIO.input(23) == 1):
		if countTime <= 1:
			countE = countE + 1
			if countE == 1:
				print('E')
				char = 'E'
				soulName = soulName + char;
				print soulName
				time.sleep(waiting)
				countOuija = 0
				countH = 0
				countI = 0
				countT = 0
				countL = 0
				countR = 0
				countTime = 0

	if(GPIO.input(25) == 1):
		countTime = countTime + 1
		if countTime <= 1:
			countR = countR + 1
			if countR == 1:
				print('R')
				char = 'R'
				soulName = soulName + char;
				print soulName
				time.sleep(waiting)
				countOuija = 0
				countH = 0
				countI = 0
				countT = 0
				countL = 0
				countE = 0
				countTime = 0			

GPIO.cleanup()

########################################################
########################################################

if searchState == 1:
	
	########################################################################################
	#wait for the name of the soul to be invoked and search it using the GOOGLE SEARCH API
	countSoulName = 0
	print "////////////////////////////////////////////////////"
	#print "The name of the soul is: " + soulName 
	#print "////////////////////////////////////////////////////"
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

	
