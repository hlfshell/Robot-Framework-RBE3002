'''
TurretClass.py

Author: Keith Chester

Turrets are objects comprised of infrared
sensors and servos (or steppers). They are
children of both actuator and sensor class.

The additional function of a turret class is
its pan() function, which will create and return
a list of polar coordinate readings (angle, magnitude)
of what the turret sees in front of it.

This class was created for a more abstracted and
easily organized view of a turret/sensor platform.

'''

import serial, time
from Commands import *
from ActuatorClass import *
from SensorClass import *
from InfraredClass import *
from ServoClass import *

class Turret(Actuator, Sensor):

	infrared = None
	servo = None

	def __init__(self, servoInstance, infraredInstance):
		global setServoTo
		self.infrared = infraredInstance
		self.servo = servoInstance
		

	def pan(self):
		if self.servo.Position > 90:
			self.servo.moveTo(165)
			time.sleep(.1)
			b = range(165,13, -2)
		else:
			self.servo.moveTo(15)
			time.sleep(.1)
			b = range(15, 167, 2)
		endResult = []
		positionTemp = self.servo.Position
		for i in b:
			self.servo.moveTo(i)
			time.sleep(.01)
			endResult.append([self.servo.Position, self.infrared.grabData()])
			positionTemp = self.servo.Position
		return endResult

	def moveTo(self, position):
		self.servo.moveTo(position)

	def readAt(self, position):
		oldPosition = self.servo.Position
		self.moveTo(position)
		#Build a time delay that is based on the approximate time it will take to travel.
		#For this I have assumed 3 seconds to go the whole 180 degrees.
		time.sleep(.005)
		return [self.servo.Position, self.infrared.grabData()]
		
