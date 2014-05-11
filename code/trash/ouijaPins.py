# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(25, GPIO.IN)

while True:

	if(GPIO.input(4) ==1):
		print('OUIJA')

	if(GPIO.input(17) == 1):
		print('H')

	if(GPIO.input(18) ==1):
		print('I')

	if(GPIO.input(27) == 1):
		print('T')

	if(GPIO.input(22) ==1):
		print('L')

	if(GPIO.input(23) == 1):
		print('E')

	if(GPIO.input(25) == 1):
		print('R')			

GPIO.cleanup()
