#! /usr/env/bin python

'''

'''

import sys, time, string
from numpy import *

class Map:

	worldMap = zeros([200, 200])

	#robotInformation = origin, orientation, dimensions
	robotInformation = None

	robotOrigin = startPos

	def __init__(self, mapDimensions, robotStartPoint):
		self.

	def removeRobot(self):
		pass

	def placeRobot(self):
		pass

	def addObstacle(self, angle, magnitude, sensorErrorMagnitude):
		pass

	def update(self):
		pass
		#read encoder values. Figure out robot information
		#update robot information
		#remove robot from map
		#place new robot
		#Pan the infrared. Get readings.
		#step through readings, add to map
