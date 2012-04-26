'''
StepperClass.py

Author: Keith Chester

Creates and maintains a stepper object.

Allows steppers to request a particular position
for the stepper, maintained by the robot side.

'''

import serial
from Commands import *
from ActuatorClass import *

class Stepper:

	def __init__(self, connectionInstance):
		global sendStepperTo
		self.serialConnection = connectionInstance
		self.Command = sendStepperTo

	def moveTo(self, position):
		global SendStepperTo
		littleOne.serialConnection.write(sendStepperTo)
		littleOne.serialConnection.write(position)
		littleOne.serialConnection.write((position >> 8))

