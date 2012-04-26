'''
BumperClass.py

Author: Keith Chester

A bumper object, it reads either a 0 or 1
from the appropiate pin on the robot. This is
compared to activeOn to see if the bumper is active
or not (as bumpers are either active low (0) or active
high (1).

'''

from SensorClass import *
from Commands import *


class Bumper(Sensor):

	activeOn = 0
	isActive = True

	'''__init__(connectionInstance, pin = 0)
		Given a serial connection and possibly a
		pin value, create a Bumper object.
	'''
	def __init__(self, connectionInstance, pin = 0):
		self.serialConnection = connectionInstance
		global requestPinValue
		self.historyToRemember = 1
		self.bytesPerData = 1
		self.PinOrChannel = pin
		self.Command = requestPinValue

	'''
	isHit()
		Checks the value of the bumper against the
		bumper's "activeOn" value (ie: active low
		or active high. By default bumpers are active
		low). It returns true or false based on the
		comparison.
	@return boolean - true if hit, false if not
	'''
	def isHit(self):
		rawCheck = self.readData()
		if rawCheck == self.activeOn:
			self.isActive = True
		else:
			self.isActive = False
		return self.isActive

	'''
	grabData()
		A general function call for easy calling of multiple unknown
		components by AI.
	@return whatever that object returns
	'''
	def grabData(self):
		return self.isHit()
