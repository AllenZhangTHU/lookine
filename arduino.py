import serial
import time
import math

device = '/dev/ttyUSB0'
try:
	arduino = serial.Serial(device, 9600)
except:
	print 'Failed to connect on ' + devide

margin = 50
moveUnit = 5
while True:
	ctrlSignal = getSignal()
	if (abs(ctrlSignal) < margin):
		continue
	ctrlSignal /= abs(ctrlSignal)
	ctrlSignal *= moveUnit
	try:
		arduino.write(str(ctrlSignal))
		time.sleep(1)
		print arduino.readline()
	except:
		print 'Failed to send'

