'''
ServoClass.py

Author: Keith Chester

A servo object, child of the actuator class,
takes a given angle, converts the value to a
servo pulse, and notifies hardware of the change.

It maintains control over movement of the servo.

'''

import serial, time
from Commands import *
from ActuatorClass import *
from InfraredClass import *

class Servo(Actuator):

	def __init__(self, connectionInstance):
		global setServoTo
		self.serialConnection = connectionInstance
		self.Command = setServoTo

	def moveTo(self, position):
		global setServoTo
		position = position
		if position < 0:
			position = 0
		elif position > 180:
			position = 180
		self.Position = position
		difference = (2400 - 550) / 180
		position = (position + 9) * difference
		position = int(position + 550)
		self.serialConnection.write(setServoTo)
		self.serialConnection.write(chr(position/10))		
	
	'''def pan(self, infrared):
		direction = 1
		if self.Position > 90:
			self.moveTo(165)
			direction = -1
			b = range(165,0,-2)
		else:
			self.moveTo(0)
			direction = 1
			b = range(0, 165, 2)
		endResult = []
		positionTemp = self.Position
		for i in b:
			self.moveTo(positionTemp + (direction * 2) )
			endResult.append(infrared.grabData())
			time.sleep(.0025)
			positionTemp = self.Position
		if direction == 1:
			self.moveTo(165)
		else:
			self.moveTo(0)
		return endResult'''
