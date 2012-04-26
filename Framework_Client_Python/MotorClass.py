'''
MotorClass.py

Author: Keith Chester

Creates and maintains control over an individual motor.

'''

import serial
from Commands import *
from ActuatorClass import *

class Motor(Actuator):
	
	side = None

	'''__init__(connectionInstance, sideInstanace)
		Given a serial connection and a side (left or right),
		create a motor object.
	'''
	def __init__(self, connectionInstance, sideInstance):
		global setMotorRight, setMotorLeft
		self.serialConnection = connectionInstance
		self.side = sideInstance
		if self.side == 'left': self.Command = setMotorLeft
		elif self.side == 'right': self.Command = setMotorRight

	'''setVoltage(voltage)
		Sets the motor's voltage to the appropiate value.
	@param voltage - a value of what voltage you wish to that motor to.
	'''
	def setVoltage(self, voltage):
		self.serialConnection.write(self.Command)
		self.serialConnection.write(chr(voltage/10))

	'''setMotor(percentage)
		Given a percentage, move the motor the correct direction and magnitude.
	@param voltage - a percentage, -100 to 100, of what speed and direction you want the motor to run at
	'''
	def setMotor(self, percentage):
		global setMotorLeftForward, setMotorRightForward, setMotorLeftReverse, setMotorRightReverse
		tmp = percentage
		percentage = float(abs(percentage))
		valueOut = int(((percentage/100) * 2048) / 10)
		if tmp >= 0:
			if self.side == 'left':
				self.serialConnection.write(setMotorLeftForward)
				self.serialConnection.write(chr(valueOut))
			if self.side == 'right':
				self.serialConnection.write(setMotorRightForward)
				self.serialConnection.write(chr(valueOut))
		if tmp < 0:
			if self.side == 'left':
				self.serialConnection.write(setMotorLeftReverse)
				self.serialConnection.write(chr(valueOut))
			if self.side == 'right':
				self.serialConnection.write(setMotorRightReverse)
				self.serialConnection.write(chr(valueOut))

