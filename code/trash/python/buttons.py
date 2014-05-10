import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
	if (GPIO.input(23) == 1):
		
		print("Button1 PRESSED")
		
	if (GPIO.input(24) == 0):
		print("Button2 PRESSED")
	
	time.sleep(0.2)
	
GPIO.cleanup()
