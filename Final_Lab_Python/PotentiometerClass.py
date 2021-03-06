'''
PotentiometerClass.py

Author: Keith Chester

Creates a potentiometer object, a sensor of 2 bytes
that reads from the robot's ADC. Readings can be converted
to an angle.

'''

from SensorClass import *
from Commands import *


class Potentiometer(Sensor):

	theta = 0
	conversionMultiplier = 1
	conversionOffset = 0

	def __init__(self, connectionInstance, channel= 0, conversionMultiplierInstance = 1, conversionOffsetInstance = 0):
		self.serialConnection = connectionInstance
		global requestADCchannel
		self.historyToRemember = 1
		self.bytesPerData = 2
		self.PinOrChannel = channel
		self.Command = requestADCchannel
		self.conversionMultiplier = conversionMultiplierInstance
		self.conversionOffset = conversionOffsetInstance

	'''
	getTheta()
		getTheta gets the potentiometer's raw read, multiplies
		it by the potentiometer's conversion multiplier (an
		attribute), and then adds its conversion offset to it.
		The result should be a linear angle conversion from the
		potentiometer.
	@return  theta - the angle of the potentiometer
	'''
	def getTheta(self):
		rawRead = self.readData()
		self.theta = (rawRead * self.conversionMultiplier) + self.conversionOffset
		return self.theta

	'''
	grabData()
		A general function call for easy calling of multiple unknown
		components by AI.
	@return whatever that object returns
	'''
	def grabData(self):
		return self.getTheta()
