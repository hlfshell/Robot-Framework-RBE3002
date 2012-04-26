'''
SensorClass.py

Author: Keith Chester

The parent class for all sensors, sensor class
most importantly creates a standard for grabbing N
bytes of data from the robot based on the sensor it
is updating.

'''

import serial
from Commands import *

class Sensor:
	
	data = None
	historyToRemember = 10
	bytesPerData = 1
	PinOrChannel = 0
	serialConnection = None
	Command = None

	def __init__(self, connectionInstance):
		self.serialConnection = connectionInstance

	def readData(self):
		self.serialConnection.write(self.Command)
		self.serialConnection.write(chr(self.PinOrChannel))
		self.data = self.serialConnection.read(self.bytesPerData)
		while self.data is None:
			self.data = self.serialConnection.read(self.bytesPerData)
		tmp = 0
		try:
			for i in range(0,self.bytesPerData):
				tmp = tmp + (ord(self.data[i]) << (8*i))
		except:
			print 'Sensor read failure!'
		return tmp

