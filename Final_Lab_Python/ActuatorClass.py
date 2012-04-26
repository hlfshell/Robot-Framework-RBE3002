'''
ActuatorClass.py

Author: Keith Chester

The general class for all actuators.

'''

import serial
from Commands import *

class Actuator:
	
	serialConnection = None
	Command = None
	hasPID = False

	#Calculated values for each actuator for potential calculations
	Position = 0
	Velocity = None

	#Control values for future feedback control loops
	Kp = None
	Ki = None
	Kd = None
	
	'''__init__(connectionInstance)
		Given a serial connection, create an actuator.
	'''
	def __init__(self, connectionInstance):
		self.serialConnection = connectionInstance

	''' setPID(KpInstance, KiInstance = 0, KdInstance = 0)
		Set these variables in this object and send them
		to the robot to apply to a control feedback loop.
	'''
	def setPID(self, KpInstance, KiInstance = 0, KdInstance = 0):
		global setPID
		self.serialConnection.write(setPID)
		self.serialConnection.write(chr(KpInstance))
		self.serialConnection.write(chr(KiInstance))
		self.serialConnection.write(chr(KdInstnace))
