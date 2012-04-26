'''
InfraredClass.py

Author: Keith Chester

A child of the Sensor class, an infrared sensor
is an object that receives an ADC reading (2 bytes)
and convers it to a reading of 0 to 80 cm. Note:
0 cm is reported upon no detection made.

'''

from SensorClass import *
from Commands import *


class Infrared(Sensor):

	distance = 0

	'''__init__(connectionInstance, channel = 0)
		Given a serial connection and possibly a
		channel value, create an Infrared object.
	'''
	def __init__(self, connectionInstance, channel= 0):
		self.serialConnection = connectionInstance
		global requestADCchannel
		self.historyToRemember = 1
		self.bytesPerData = 2
		self.PinOrChannel = channel
		self.Command = requestADCchannel
		

	'''
	getTheta()
		getTheta gets the potentiometer's raw read, multiplies
		it by the potentiometer's conversion multiplier (an
		attribute), and then adds its conversion offset to it.
		The result should be a linear angle conversion from the
		potentiometer.
	@return  theta - the angle of the potentiometer
	'''
	def getDistance(self):
		rawRead = self.readData()
		if rawRead <= 3:
			self.distance = 0
		else:
			self.distance = (6787 / (rawRead - 3)) - 4
		if self.distance >= 80:
			self.distance = 0
		return self.distance

	'''
	grabData()
		A general function call for easy calling of multiple unknown
		components by AI.
	@return whatever that object returns
	'''
	def grabData(self):
		return self.getDistance()
